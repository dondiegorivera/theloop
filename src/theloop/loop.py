"""Loop — the main control flow.

For each iteration N:

  1. Workspace.begin_iteration(N)    — checkout parent branch
  2. Orchestrator.plan(spec, prev_critique)  → updated spec + iteration intent
  3. Orchestrator.direct(intent, ws, adapter_notes) → prompt for pi
  4. PiClient.prompt(prompt) → assistant text + touched files
  5. Adapter.runtime_check(ws) → ok/fail (failure feeds into next plan, no render)
  6. Adapter.render(ws, png) → screenshot (skipped if !has_visual_artifact or rc fail)
  7. Judge.evaluate(spec, png, pi_text) → verdict
  8. Workspace.commit_iteration(N, intent) → branch iter/N
  9. Reporter.emit(...) at every boundary
 10. Terminator.should_stop(history) — break if not None

The Loop owns no LLM state. All persistence is in Workspace + Reporter.
"""

from __future__ import annotations

import asyncio
import contextlib
import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path

from theloop.adapters.base import RuntimeCheckResult, TaskAdapter
from theloop.judge import Judge, JudgeVerdict
from theloop.orchestrator import Orchestrator, PlanResult
from theloop.pi_client import PiClient, PiResult
from theloop.renderer import Renderer
from theloop.reporter import Reporter
from theloop.terminator import StopReason, Terminator
from theloop.workspace import Workspace

log = logging.getLogger(__name__)
_WRITE_TOOL_NAMES = {"edit", "write", "create", "Edit", "Write", "Create"}
_LATER_ITER_PREWRITE_TOOL_LIMIT = 8
_RETRY_PREWRITE_TOOL_LIMIT = 4


@dataclass(frozen=True, slots=True)
class IterationRecord:
    iter: int
    intent: str
    spec: str  # planner's updated spec going into pi/judge for this iter
    pi_assistant_text: str
    pi_touched: list[Path]
    runtime_check: RuntimeCheckResult
    render_png: Path | None
    verdict: JudgeVerdict
    commit_sha: str | None


@dataclass(frozen=True, slots=True)
class RunResult:
    run_id: str
    run_dir: Path
    stop_reason: StopReason
    best_score: float | None
    iterations: list[IterationRecord]


class Loop:
    def __init__(
        self,
        spec: str,
        adapter: TaskAdapter,
        adapter_notes: str,
        orchestrator: Orchestrator,
        pi_factory,  # () -> PiClient context manager (one per iteration)
        renderer: Renderer | None,
        judge: Judge,
        terminator: Terminator,
        workspace: Workspace,
        reporter: Reporter,
        *,
        pi_timeout_s: float = 600.0,
        pi_no_write_timeout_s: float = 0.0,
    ) -> None:
        self.spec = spec
        self.adapter = adapter
        self.adapter_notes = adapter_notes
        self.orchestrator = orchestrator
        self.pi_factory = pi_factory
        self.renderer = renderer
        self.judge = judge
        self.terminator = terminator
        self.workspace = workspace
        self.reporter = reporter
        self.pi_timeout_s = pi_timeout_s
        self.pi_no_write_timeout_s = pi_no_write_timeout_s

    async def run(self) -> RunResult:
        rep = self.reporter
        # Persist the original (user-authored) spec at the run root. The
        # report builder reads it back into the header so anyone opening
        # the report can see what the user actually asked for, not just
        # the planner's evolved version. spec.md inside artifacts/iter-N/
        # is the planner's output; this is the source.
        try:
            (self.workspace.run_dir / "spec.md").write_text(self.spec)
        except Exception as e:
            log.debug("could not persist original spec: %s", e)
        rep.emit(
            "run_start",
            run_id=self.workspace.run_dir.name,
            adapter=self.adapter.name,
            spec_chars=len(self.spec),
            max_iters=self.terminator.config.max_iters,
            score_threshold=self.terminator.config.score_threshold,
            no_improvement_for=self.terminator.config.no_improvement_for,
        )

        # iter 0 starts from the adapter's scaffold.
        self.workspace.begin_iteration(0)
        self.adapter.prepare(self.workspace.workspace_path)
        rep.emit("scaffold", iter=0, files=[
            str(p.relative_to(self.workspace.workspace_path))
            for p in self.workspace.workspace_path.rglob("*")
            if p.is_file() and ".git" not in p.parts
        ])

        history: list[JudgeVerdict] = []
        records: list[IterationRecord] = []
        spec = self.spec
        prev_critique: str | None = None
        prev_description: str | None = None
        stop: StopReason | None = None

        for it in range(self.terminator.config.max_iters):
            if it > 0:
                self.workspace.begin_iteration(it)

            prev_verdict = history[-1] if history else None
            rec = await self._run_one(
                it, spec, prev_critique, prev_description, prev_verdict
            )
            records.append(rec)
            history.append(rec.verdict)
            spec = rec.spec  # carry the planner's updated spec forward
            prev_critique = _critique_for_next_plan(
                rec.verdict,
                score_threshold=self.terminator.config.score_threshold,
            )
            prev_description = rec.verdict.description or None

            stop = self.terminator.should_stop(history)
            rep.emit(
                "iter_end",
                iter=it,
                score=rec.verdict.score,
                done=rec.verdict.done,
                stop=stop.value if stop else None,
            )
            if stop is not None:
                break

        if stop is None:
            stop = StopReason.MAX_ITERS

        scores = [v.score for v in history if v.score is not None]
        best = max(scores) if scores else None

        rep.emit("run_end", reason=stop.value, best_score=best, iters_run=len(records))
        return RunResult(
            run_id=self.workspace.run_dir.name,
            run_dir=self.workspace.run_dir,
            stop_reason=stop,
            best_score=best,
            iterations=records,
        )

    # ── per-iteration -----------------------------------------------------

    async def _run_one(
        self,
        it: int,
        spec_in: str,
        prev_critique: str | None,
        prev_description: str | None,
        prev_verdict: JudgeVerdict | None,
    ) -> IterationRecord:
        rep = self.reporter
        ws = self.workspace
        ws_path = ws.workspace_path

        # 1. plan -----------------------------------------------------------
        rep.emit("plan_start", iter=it)
        plan: PlanResult = await self.orchestrator.plan(
            spec_in, prev_critique, prev_description
        )
        rep.emit("plan_end", iter=it, intent=plan.intent, spec_chars=len(plan.spec))

        # 2. direct ---------------------------------------------------------
        rep.emit("direct_start", iter=it)
        pi_prompt = await self.orchestrator.direct(
            plan.spec, plan.intent, ws_path, self.adapter_notes
        )
        rep.emit("direct_end", iter=it, prompt_chars=len(pi_prompt))

        # 3. pi -------------------------------------------------------------
        rep.emit("pi_start", iter=it)
        pi_result: PiResult = await self._run_pi_with_retry(it, pi_prompt)
        rep.emit(
            "pi_end",
            iter=it,
            event_count=pi_result.event_count,
            tool_calls=len(pi_result.tool_calls),
            touched=[str(p) for p in pi_result.touched_files],
            assistant_chars=len(pi_result.assistant_text),
        )
        reconciled = ws.reconcile_external_writes(list(pi_result.touched_files))
        if reconciled:
            rep.emit(
                "pi_reconciled_writes",
                iter=it,
                files=[
                    {"from": str(src), "to": str(dest.relative_to(ws_path))}
                    for src, dest in reconciled
                ],
            )

        if it > 0 and prev_verdict is not None and not ws.repo.git.diff():
            rep.emit("pi_no_workspace_changes", iter=it)
            rc = RuntimeCheckResult(ok=True, log="no workspace changes; reused previous verdict")
            rep.emit("runtime_check", iter=it, ok=rc.ok, log=rc.log)
            rep.emit(
                "judge_end",
                iter=it,
                **_verdict_payload(prev_verdict),
                reused=True,
            )
            sha = ws.commit_iteration(it, plan.intent)
            rep.emit("commit", iter=it, sha=sha, branch=f"iter/{it}")
            try:
                artifact_dir = ws.artifact_dir(it)
                (artifact_dir / "spec.md").write_text(plan.spec)
                (artifact_dir / "pi_prompt.txt").write_text(pi_prompt)
                (artifact_dir / "pi_assistant.txt").write_text(
                    pi_result.assistant_text
                )
                artifact_text = self.adapter.artifact_text(ws_path)
                if artifact_text:
                    (artifact_dir / "artifact.txt").write_text(artifact_text)
                if prev_verdict.description:
                    (artifact_dir / "judge_description.txt").write_text(
                        prev_verdict.description
                    )
                (artifact_dir / "verdict.json").write_text(
                    json.dumps(_verdict_payload(prev_verdict), indent=2)
                )
            except Exception as e:
                log.debug("could not persist no-op iter %d artifacts: %s", it, e)
            return IterationRecord(
                iter=it,
                intent=plan.intent,
                spec=plan.spec,
                pi_assistant_text=pi_result.assistant_text,
                pi_touched=list(pi_result.touched_files),
                runtime_check=rc,
                render_png=None,
                verdict=prev_verdict,
                commit_sha=sha,
            )

        # 4. runtime check --------------------------------------------------
        rc = self.adapter.runtime_check(ws_path)
        rep.emit("runtime_check", iter=it, ok=rc.ok, log=rc.log)

        # 5. render ---------------------------------------------------------
        png_path: Path | None = None
        if rc.ok and self.adapter.has_visual_artifact and self.renderer is not None:
            png_path = ws.artifact_dir(it) / "render.png"
            try:
                await self.adapter.render(ws_path, png_path, self.renderer)
                rep.emit("render", iter=it, png=str(png_path), bytes=png_path.stat().st_size)
            except Exception as e:  # render failure is non-fatal; judge sees no image.
                log.warning("iter %d: render failed: %s", it, e)
                rep.emit("render_error", iter=it, error=str(e))
                png_path = None

        # 6. judge ----------------------------------------------------------
        judge_png = png_path if (rc.ok and png_path is not None) else None
        artifact_text = self.adapter.artifact_text(ws_path) if rc.ok else None
        judge_profile = self.adapter.judge_profile()
        if artifact_text:
            try:
                (ws.artifact_dir(it) / "artifact.txt").write_text(artifact_text)
            except Exception as e:
                log.debug("could not persist iter %d text artifact: %s", it, e)
        rep.emit(
            "judge_start",
            iter=it,
            has_image=bool(judge_png),
            artifact_chars=len(artifact_text) if artifact_text else 0,
            profile=judge_profile,
        )
        verdict = await self.judge.evaluate(
            spec=plan.spec,
            png_path=judge_png,
            last_pi_output=pi_result.assistant_text,
            artifact_text=artifact_text,
            score_threshold=self.terminator.config.score_threshold,
            judge_profile=judge_profile,
        )
        rep.emit(
            "judge_end",
            iter=it,
            **_verdict_payload(verdict),
        )

        # 7. commit ---------------------------------------------------------
        sha: str | None = None
        try:
            sha = ws.commit_iteration(it, plan.intent)
            rep.emit("commit", iter=it, sha=sha, branch=f"iter/{it}")
        except Exception as e:
            log.warning("iter %d: git commit failed: %s", it, e)
            rep.emit("commit_error", iter=it, error=str(e))

        # Persist the per-iter spec snapshot for the report.
        try:
            artifact_dir = ws.artifact_dir(it)
            (artifact_dir / "spec.md").write_text(plan.spec)
            (artifact_dir / "pi_prompt.txt").write_text(pi_prompt)
            (artifact_dir / "pi_assistant.txt").write_text(pi_result.assistant_text)
            if artifact_text:
                (artifact_dir / "artifact.txt").write_text(artifact_text)
            if verdict.description:
                (artifact_dir / "judge_description.txt").write_text(verdict.description)
            (artifact_dir / "verdict.json").write_text(
                json.dumps(_verdict_payload(verdict), indent=2)
            )
        except Exception as e:
            log.debug("could not persist iter %d artifacts: %s", it, e)

        return IterationRecord(
            iter=it,
            intent=plan.intent,
            spec=plan.spec,
            pi_assistant_text=pi_result.assistant_text,
            pi_touched=list(pi_result.touched_files),
            runtime_check=rc,
            render_png=png_path,
            verdict=verdict,
            commit_sha=sha,
        )

    async def _run_pi_with_retry(self, it: int, prompt: str) -> PiResult:
        try:
            return await self._run_pi(it, prompt, attempt=0)
        except TimeoutError as first_error:
            if self.pi_no_write_timeout_s <= 0:
                raise
            retry_prompt = _compose_pi_retry_prompt(prompt)
            self.reporter.emit(
                "pi_retry_start",
                iter=it,
                reason=str(first_error),
                prompt_chars=len(retry_prompt),
            )
            try:
                return await self._run_pi(it, retry_prompt, attempt=1)
            except TimeoutError as second_error:
                self.reporter.emit(
                    "pi_retry_failed",
                    iter=it,
                    reason=str(second_error),
                )
                return PiResult(
                    assistant_text=(
                        f"pi timed out before making a write/edit/create call: "
                        f"{second_error}"
                    ),
                    tool_calls=[],
                    touched_files=[],
                    event_count=0,
                    messages=[],
                )

    async def _run_pi(self, it: int, prompt: str, *, attempt: int) -> PiResult:
        rep = self.reporter
        started = time.monotonic()
        stats = {"events": 0, "tools": 0, "write_tools": 0, "last_type": "(none)"}
        prompt_task: asyncio.Task[PiResult] | None = None
        live_state: dict[str, object] = {}
        live_log_name = "pi_live.log" if attempt == 0 else f"pi_live_retry{attempt}.log"
        live_log_path = self.workspace.artifact_dir(it) / live_log_name
        live_log = live_log_path.open("w", buffering=1)
        live_log.write(f"# pi activity log for iter {it}, attempt {attempt}\n")
        live_log.write(f"# prompt_chars={len(prompt)}\n\n")
        rep.emit("pi_live_log", iter=it, path=str(live_log_path))

        async def heartbeat() -> None:
            while True:
                await asyncio.sleep(30.0)
                elapsed = time.monotonic() - started
                rep.emit(
                    "pi_progress",
                    iter=it,
                    elapsed_s=round(elapsed, 1),
                    events=stats["events"],
                    tools=stats["tools"],
                    write_tools=stats["write_tools"],
                    last_type=stats["last_type"],
                    phase="waiting",
                )
                if (
                    it > 0
                    and self.pi_no_write_timeout_s > 0
                    and stats["write_tools"] == 0
                    and elapsed >= self.pi_no_write_timeout_s
                    and prompt_task is not None
                    and not prompt_task.done()
                ):
                    rep.emit(
                        "pi_no_write_timeout",
                        iter=it,
                        elapsed_s=round(elapsed, 1),
                        timeout_s=self.pi_no_write_timeout_s,
                        events=stats["events"],
                        tools=stats["tools"],
                        last_type=stats["last_type"],
                    )
                    prompt_task.cancel()
                    return

        def on_event(event: dict) -> None:
            stats["events"] += 1
            etype = str(event.get("type") or "(unknown)")
            stats["last_type"] = etype
            _write_pi_live_event(
                live_log,
                event,
                state=live_state,
                elapsed_s=time.monotonic() - started,
            )

            if etype == "tool_execution_start":
                stats["tools"] += 1
                if event.get("toolName") in _WRITE_TOOL_NAMES:
                    stats["write_tools"] += 1
                args = event.get("arguments") or event.get("args") or {}
                if stats["write_tools"] == 0:
                    violation = _prewrite_policy_violation(
                        it=it,
                        attempt=attempt,
                        tool=str(event.get("toolName") or ""),
                        args=args,
                        tool_count=int(stats["tools"]),
                        workspace=self.workspace.workspace_path,
                    )
                    if violation:
                        rep.emit(
                            "pi_prewrite_policy_warning",
                            iter=it,
                            elapsed_s=round(time.monotonic() - started, 1),
                            reason=violation,
                            events=stats["events"],
                            tools=stats["tools"],
                            last_type=etype,
                        )
                rep.emit(
                    "pi_tool_start",
                    iter=it,
                    elapsed_s=round(time.monotonic() - started, 1),
                    tool=event.get("toolName"),
                    args=_summarize_tool_args(args),
                    events=stats["events"],
                    tools=stats["tools"],
                    write_tools=stats["write_tools"],
                )
            elif etype == "tool_execution_end":
                rep.emit(
                    "pi_tool_end",
                    iter=it,
                    elapsed_s=round(time.monotonic() - started, 1),
                    tool=event.get("toolName"),
                    events=stats["events"],
                    tools=stats["tools"],
                    write_tools=stats["write_tools"],
                )
            elif stats["events"] % 1000 == 0:
                rep.emit(
                    "pi_progress",
                    iter=it,
                    elapsed_s=round(time.monotonic() - started, 1),
                    events=stats["events"],
                    tools=stats["tools"],
                    write_tools=stats["write_tools"],
                    last_type=etype,
                    phase="streaming",
                )
                elapsed = time.monotonic() - started
                if (
                    it > 0
                    and self.pi_no_write_timeout_s > 0
                    and stats["write_tools"] == 0
                    and elapsed >= self.pi_no_write_timeout_s
                ):
                    rep.emit(
                        "pi_no_write_timeout",
                        iter=it,
                        elapsed_s=round(elapsed, 1),
                        timeout_s=self.pi_no_write_timeout_s,
                        events=stats["events"],
                        tools=stats["tools"],
                        last_type=etype,
                    )
                    raise TimeoutError(
                        f"pi made no write/edit/create call within "
                        f"{self.pi_no_write_timeout_s:.0f}s"
                    )

        async with self.pi_factory() as pi:
            await pi.new_session()
            beat = asyncio.create_task(heartbeat())
            try:
                prompt_task = asyncio.create_task(
                    pi.prompt(prompt, on_event=on_event, timeout=self.pi_timeout_s)
                )
                return await prompt_task
            except TimeoutError:
                rep.emit(
                    "pi_timeout",
                    iter=it,
                    elapsed_s=round(time.monotonic() - started, 1),
                    timeout_s=self.pi_timeout_s,
                    events=stats["events"],
                    tools=stats["tools"],
                    write_tools=stats["write_tools"],
                    last_type=stats["last_type"],
                )
                raise
            except asyncio.CancelledError as e:
                raise TimeoutError(
                    f"pi made no write/edit/create call within "
                    f"{self.pi_no_write_timeout_s:.0f}s"
                ) from e
            finally:
                beat.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await beat
                live_log.close()


def _summarize_tool_args(args: object, *, max_chars: int = 500) -> object:
    if not isinstance(args, dict):
        return str(args)[:max_chars]
    summary: dict[str, object] = {}
    for key, value in args.items():
        if key in {"content", "new_string", "old_string", "text"} and isinstance(value, str):
            summary[key] = f"<{len(value)} chars>"
        else:
            s = str(value)
            summary[key] = s[:max_chars] + ("..." if len(s) > max_chars else "")
    return summary


def _verdict_payload(verdict: JudgeVerdict) -> dict[str, object]:
    return {
        "score": verdict.score,
        "done": verdict.done,
        "critique": verdict.critique,
        "description_chars": len(verdict.description),
        "hard_failures": verdict.hard_failures or [],
        "dimensions": verdict.dimensions or {},
        "next_action": verdict.next_action,
        "regression_against_best": verdict.regression_against_best,
    }


def _critique_for_next_plan(
    verdict: JudgeVerdict,
    *,
    score_threshold: float,
) -> str | None:
    critique = verdict.critique.strip() if verdict.critique else ""
    if (
        verdict.done
        and verdict.score is not None
        and verdict.score < score_threshold
    ):
        note = (
            f"Previous judge returned done=true at score {verdict.score:.2f}, "
            f"below the configured threshold {score_threshold:.2f}. Do not "
            "verify, conclude, or make vague final polish. Choose one concrete "
            "visible artifact improvement that changes the output, prioritizing "
            "legibility, containment of text within its surface, spatial "
            "coherence, action clarity, and composition."
        )
        return f"{critique}\n\n{note}" if critique else note
    return critique or None


def _prewrite_policy_violation(
    *,
    it: int,
    attempt: int,
    tool: str,
    args: object,
    tool_count: int,
    workspace: Path | None = None,
) -> str | None:
    """Bound read-only pi loops before they consume a full timeout window."""
    if it <= 0:
        return None
    limit = _RETRY_PREWRITE_TOOL_LIMIT if attempt > 0 else _LATER_ITER_PREWRITE_TOOL_LIMIT
    if tool_count > limit:
        return (
            f"pi used {tool_count} tools without calling write/edit/create "
            f"(limit {limit})"
        )
    if tool == "read" and isinstance(args, dict):
        path = str(args.get("path") or args.get("file_path") or "")
        has_limit = "limit" in args and str(args.get("limit") or "").strip()
        if path.endswith("generate_artifact.py") and not has_limit:
            if _is_small_workspace_file(path, workspace):
                return None
            return (
                "pi attempted an unbounded read of generate_artifact.py before "
                "making a write/edit/create call"
            )
    return None


def _is_small_workspace_file(path: str, workspace: Path | None) -> bool:
    """Allow full reads of tiny scaffold files, not large generated helpers."""
    if workspace is None:
        return False
    p = Path(path)
    target = p if p.is_absolute() else workspace / p
    try:
        resolved = target.resolve()
        resolved.relative_to(workspace.resolve())
        return resolved.is_file() and resolved.stat().st_size <= 12_000
    except OSError:
        return False
    except ValueError:
        return False


def _compose_pi_retry_prompt(original_prompt: str) -> str:
    directive = _section(original_prompt, "## Iteration directive", "## Execution rule")
    spec_hint = _section(original_prompt, "## Authoritative spec", "## Iteration directive")
    if len(spec_hint) > 1800:
        spec_hint = spec_hint[:1800].rstrip() + "\n...(spec truncated for retry)"
    return (
        "Your previous turn timed out before calling `write`, `edit`, or "
        "`create`. Do not analyze the whole artifact again.\n\n"
        "## Task\n"
        f"{directive.strip() or '(use the previous iteration directive)'}\n\n"
        "## Minimal spec reminder\n"
        f"{spec_hint.strip()}\n\n"
        "## Required action now\n"
        "1. Make the smallest concrete edit that addresses the task. At most "
        "one locating `rg`/`grep` command is allowed before the edit.\n"
        "2. For SVG generator tasks, edit `generate_artifact.py` only, then run "
        "`python generate_artifact.py`.\n"
        "3. Do not read full `artifact.svg`; it is generated output.\n"
        "4. Do not read the full generator. Do not use broad inspection as a "
        "separate phase; locate, edit, regenerate.\n"
        "5. Use relative paths only, including in bash commands. Do not `cd` "
        "to `/src/...` or reference any absolute workspace path.\n"
        "6. Do not install packages or create preview images. Run one targeted "
        "validation command, then stop."
    )


def _section(text: str, start: str, end: str) -> str:
    start_idx = text.find(start)
    if start_idx == -1:
        return ""
    start_idx += len(start)
    end_idx = text.find(end, start_idx)
    if end_idx == -1:
        end_idx = len(text)
    return text[start_idx:end_idx].strip()


def _write_pi_live_event(
    fh,
    event: dict,
    *,
    state: dict[str, object],
    elapsed_s: float,
) -> None:
    prefix = f"[{elapsed_s:7.1f}s] "
    etype = event.get("type")
    if etype == "message_update":
        delta = event.get("assistantMessageEvent") or {}
        dtype = delta.get("type")
        if dtype == "text_delta":
            _append_live_chunk(state, "text", str(delta.get("delta") or ""))
        elif dtype == "thinking_delta":
            _append_live_chunk(state, "thinking", str(delta.get("delta") or ""))
        elif dtype in {"text_start", "thinking_start"}:
            key = "thinking" if dtype == "thinking_start" else "text"
            state[f"{key}_chars"] = 0
            state[f"{key}_sample"] = ""
            fh.write(f"{prefix}[{dtype}]\n")
            fh.flush()
        elif dtype in {"text_end", "thinking_end"}:
            key = "thinking" if dtype == "thinking_end" else "text"
            chars = int(state.get(f"{key}_chars") or 0)
            sample = str(state.get(f"{key}_sample") or "").strip()
            if len(sample) > 240:
                sample = sample[:240].rstrip() + "..."
            if sample:
                fh.write(f"{prefix}[{dtype}] {chars} chars: {sample}\n")
            else:
                fh.write(f"{prefix}[{dtype}] {chars} chars\n")
            fh.flush()
        return

    if etype == "tool_execution_start":
        tool = event.get("toolName")
        args = _summarize_tool_args(event.get("arguments") or event.get("args") or {})
        fh.write(f"\n{prefix}[tool start] {tool} {args}\n")
        fh.flush()
        return

    if etype == "tool_execution_end":
        fh.write(f"{prefix}[tool end] {event.get('toolName')}\n")
        fh.flush()
        return

    if etype in {"turn_start", "turn_end", "agent_start", "agent_end"}:
        fh.write(f"\n{prefix}[{etype}]\n")
    fh.flush()


def _append_live_chunk(state: dict[str, object], key: str, chunk: str) -> None:
    if not chunk:
        return
    count_key = f"{key}_chars"
    sample_key = f"{key}_sample"
    state[count_key] = int(state.get(count_key) or 0) + len(chunk)
    sample = str(state.get(sample_key) or "")
    if len(sample) < 300:
        state[sample_key] = sample + chunk
