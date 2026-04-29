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

import logging
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

    async def run(self) -> RunResult:
        rep = self.reporter
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
        stop: StopReason | None = None

        for it in range(self.terminator.config.max_iters):
            if it > 0:
                self.workspace.begin_iteration(it)

            rec = await self._run_one(it, spec, prev_critique)
            records.append(rec)
            history.append(rec.verdict)
            spec = rec.spec  # carry the planner's updated spec forward
            prev_critique = rec.verdict.critique or None

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
    ) -> IterationRecord:
        rep = self.reporter
        ws = self.workspace
        ws_path = ws.workspace_path

        # 1. plan -----------------------------------------------------------
        rep.emit("plan_start", iter=it)
        plan: PlanResult = await self.orchestrator.plan(spec_in, prev_critique)
        rep.emit("plan_end", iter=it, intent=plan.intent, spec_chars=len(plan.spec))

        # 2. direct ---------------------------------------------------------
        rep.emit("direct_start", iter=it)
        pi_prompt = await self.orchestrator.direct(plan.intent, ws_path, self.adapter_notes)
        rep.emit("direct_end", iter=it, prompt_chars=len(pi_prompt))

        # 3. pi -------------------------------------------------------------
        rep.emit("pi_start", iter=it)
        pi_result: PiResult = await self._run_pi(pi_prompt)
        rep.emit(
            "pi_end",
            iter=it,
            event_count=pi_result.event_count,
            tool_calls=len(pi_result.tool_calls),
            touched=[str(p) for p in pi_result.touched_files],
            assistant_chars=len(pi_result.assistant_text),
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
        rep.emit(
            "judge_start",
            iter=it,
            has_image=bool(judge_png),
            artifact_chars=len(artifact_text) if artifact_text else 0,
        )
        verdict = await self.judge.evaluate(
            spec=plan.spec,
            png_path=judge_png,
            last_pi_output=pi_result.assistant_text,
            artifact_text=artifact_text,
        )
        rep.emit(
            "judge_end",
            iter=it,
            score=verdict.score,
            done=verdict.done,
            critique=verdict.critique,
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
            (ws.artifact_dir(it) / "spec.md").write_text(plan.spec)
            (ws.artifact_dir(it) / "pi_prompt.txt").write_text(pi_prompt)
            (ws.artifact_dir(it) / "pi_assistant.txt").write_text(pi_result.assistant_text)
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

    async def _run_pi(self, prompt: str) -> PiResult:
        async with self.pi_factory() as pi:
            await pi.new_session()
            return await pi.prompt(prompt, timeout=self.pi_timeout_s)
