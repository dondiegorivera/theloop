"""Subprocess + line-JSON RPC client for `pi --mode rpc`.

Pi is configured globally (~/.pi/settings.json + models.json) to use the
`mesh` provider pointing at the LiteLLM proxy. We override the model alias
per session via the --model flag; everything else (baseUrl, api key, tools)
stays at pi's defaults.

Protocol summary (from docs/pi.md):
- stdin:  one JSON object per line, e.g. {"type":"new_session"} or
          {"type":"prompt","message":"..."}
- stdout: one JSON event per line — agent_start, turn_start,
          tool_execution_start, message_update, turn_end, agent_end, etc.
          new_session and similar return a response event:
          {"type":"response","command":"new_session","success":true,...}
- stderr: pi diagnostics (compaction info, startup banners). We capture a
          ring buffer for crash diagnosis but do not parse it.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
from collections import deque
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)

EventHandler = Callable[[dict[str, Any]], Awaitable[None] | None]


class PiError(RuntimeError):
    """Pi subprocess failed or returned an error response."""


@dataclass(slots=True)
class PiResult:
    assistant_text: str
    tool_calls: list[dict[str, Any]]
    touched_files: list[Path]
    event_count: int
    messages: list[dict[str, Any]]


@dataclass(slots=True)
class _PromptCollector:
    text_parts: list[str] = field(default_factory=list)
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    touched: set[Path] = field(default_factory=set)
    messages: list[dict[str, Any]] = field(default_factory=list)
    event_count: int = 0


_FILE_KEYS = ("path", "file_path", "filePath", "filename", "target")
_WRITE_TOOLS = {"edit", "write", "create", "Edit", "Write", "Create"}


def _path_is_outside_workspace(p: Path, workspace: Path) -> bool:
    """True if `p` is absolute and falls outside `workspace`.

    Pi's model has been observed hallucinating absolute paths that *almost*
    match the workspace (truncated segments). Pi accepts them and writes
    silently outside the workspace. We can't prevent that from the client
    side, but we can detect it after the fact and warn loudly.
    """
    if not p.is_absolute():
        return False
    try:
        p.resolve().relative_to(workspace.resolve())
        return False
    except ValueError:
        return True


class PiClient:
    """Async context manager wrapping `pi --mode rpc`."""

    def __init__(
        self,
        workspace: Path,
        model_alias: str | None = None,
        thinking_level: str | None = None,
        no_session: bool = False,
        extra_args: list[str] | None = None,
        stderr_buffer: int = 200,
    ) -> None:
        self.workspace = workspace
        self.model_alias = model_alias
        self.thinking_level = thinking_level
        self.no_session = no_session
        self.extra_args = list(extra_args or [])
        self._proc: asyncio.subprocess.Process | None = None
        self._stderr_task: asyncio.Task[None] | None = None
        self._stderr_lines: deque[str] = deque(maxlen=stderr_buffer)

    # ── lifecycle ─────────────────────────────────────────────────────────

    async def __aenter__(self) -> PiClient:
        argv = ["pi", "--mode", "rpc"]
        if self.no_session:
            argv.append("--no-session")
        if self.model_alias:
            argv += ["--model", self.model_alias]
        if self.thinking_level:
            argv += ["--thinking", self.thinking_level]
        argv += self.extra_args
        log.debug("spawning pi: %s (cwd=%s)", argv, self.workspace)

        # Pi can emit very large JSON events (full message history including
        # thinking content can exceed asyncio's default 64KB readline limit).
        # Bump to 16MB; a single event over that probably indicates a bug.
        self._proc = await asyncio.create_subprocess_exec(
            *argv,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(self.workspace),
            env=os.environ.copy(),
            limit=16 * 1024 * 1024,
        )
        self._stderr_task = asyncio.create_task(self._drain_stderr())
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        proc = self._proc
        if proc is None:
            return
        try:
            if proc.stdin and not proc.stdin.is_closing():
                proc.stdin.close()
            try:
                await asyncio.wait_for(proc.wait(), timeout=3.0)
            except TimeoutError:
                proc.terminate()
                try:
                    await asyncio.wait_for(proc.wait(), timeout=2.0)
                except TimeoutError:
                    proc.kill()
                    await proc.wait()
        finally:
            if self._stderr_task:
                self._stderr_task.cancel()
            self._proc = None

    # ── public API ────────────────────────────────────────────────────────

    async def new_session(self) -> None:
        """Start a fresh pi session. Blocks until pi confirms."""
        await self._send({"type": "new_session"})
        while True:
            event = await self._read_event()
            if event is None:
                raise PiError(f"pi exited before new_session response\n{self._stderr_tail()}")
            if event.get("type") == "response" and event.get("command") == "new_session":
                if not event.get("success", False):
                    raise PiError(f"new_session failed: {event}")
                return

    async def prompt(
        self,
        text: str,
        on_event: EventHandler | None = None,
        timeout: float = 600.0,
    ) -> PiResult:
        """Send a prompt and collect events until agent_end."""
        await self._send({"type": "prompt", "message": text})
        collector = _PromptCollector()

        async def loop() -> None:
            while True:
                event = await self._read_event()
                if event is None:
                    raise PiError(f"pi exited mid-prompt\n{self._stderr_tail()}")
                collector.event_count += 1
                self._absorb(event, collector)
                if on_event is not None:
                    res = on_event(event)
                    if asyncio.iscoroutine(res):
                        await res
                if event.get("type") == "agent_end":
                    return

        await asyncio.wait_for(loop(), timeout=timeout)

        return PiResult(
            assistant_text="".join(collector.text_parts).strip(),
            tool_calls=collector.tool_calls,
            touched_files=sorted(collector.touched),
            event_count=collector.event_count,
            messages=collector.messages,
        )

    # ── internals ─────────────────────────────────────────────────────────

    async def _send(self, obj: dict[str, Any]) -> None:
        if self._proc is None or self._proc.stdin is None:
            raise PiError("pi subprocess is not running")
        line = json.dumps(obj, ensure_ascii=False) + "\n"
        self._proc.stdin.write(line.encode("utf-8"))
        await self._proc.stdin.drain()

    async def _read_event(self) -> dict[str, Any] | None:
        if self._proc is None or self._proc.stdout is None:
            return None
        raw = await self._proc.stdout.readline()
        if not raw:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            log.warning("pi: non-JSON line on stdout: %r", raw[:200])
            return await self._read_event()

    async def _drain_stderr(self) -> None:
        assert self._proc and self._proc.stderr
        while True:
            line = await self._proc.stderr.readline()
            if not line:
                return
            text = line.decode("utf-8", errors="replace").rstrip()
            self._stderr_lines.append(text)
            log.debug("pi[stderr]: %s", text)

    def _stderr_tail(self) -> str:
        return "\n".join(self._stderr_lines) or "<no stderr>"

    def _absorb(self, event: dict[str, Any], col: _PromptCollector) -> None:
        etype = event.get("type")

        if etype == "tool_execution_start":
            name = event.get("toolName")
            args = event.get("arguments") or event.get("args") or {}
            col.tool_calls.append({"name": name, "args": args})
            if name in _WRITE_TOOLS and isinstance(args, dict):
                for key in _FILE_KEYS:
                    val = args.get(key)
                    if isinstance(val, str) and val:
                        p = Path(val)
                        if _path_is_outside_workspace(p, self.workspace):
                            log.error(
                                "PI WROTE OUTSIDE WORKSPACE: tool=%s path=%r workspace=%r — "
                                "edit will not appear in workspace; check pi prompt for "
                                "stale absolute-path references",
                                name, val, str(self.workspace),
                            )
                        col.touched.add(p)
                        break
            return

        if etype == "agent_end":
            messages = event.get("messages") or []
            col.messages = messages
            for msg in messages:
                inner = msg.get("message") if "message" in msg else msg
                if not isinstance(inner, dict) or inner.get("role") != "assistant":
                    continue
                for part in inner.get("content") or []:
                    if isinstance(part, dict) and part.get("type") == "text":
                        text = part.get("text") or ""
                        if text:
                            col.text_parts.append(text)


# ── manual smoke test ───────────────────────────────────────────────────────

async def _smoke() -> None:
    """Run a trivial round-trip against pi.

    Usage:  uv run python -m theloop.pi_client
    """
    import tempfile

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    with tempfile.TemporaryDirectory(prefix="theloop-smoke-") as tmp:
        workspace = Path(tmp)
        async with PiClient(workspace=workspace) as pi:
            await pi.new_session()
            print("✓ session created")
            result = await pi.prompt(
                "Reply with exactly the word PONG and nothing else. Do not call any tools.",
                timeout=120.0,
            )
            print(f"✓ events: {result.event_count}")
            print(f"✓ tool calls: {len(result.tool_calls)}")
            print(f"✓ assistant text: {result.assistant_text!r}")


if __name__ == "__main__":
    asyncio.run(_smoke())
