"""GenericAdapter — catch-all for tasks without a visual artifact.

Used for CLI tools, data-cleaning scripts, refactors, configs, anything
where there's no single rendered surface to screenshot. The judge falls
back to text-only mode and receives text-like files from the workspace.

The adapter is deliberately minimal:

- `prepare()` writes only a `README.md` so pi knows the workspace conventions.
- `runtime_check()` is permissive: it succeeds as long as pi did *something*
  (the workspace contains at least one file beyond the scaffold). Hard
  validation of arbitrary code is out of scope; the judge handles correctness.
- `artifact_text()` collects text-like workspace files so the judge can score
  the produced artifact itself, not just pi's final summary.
- `render()` raises — `has_visual_artifact = False` means the Loop never
  calls it.
"""

from __future__ import annotations

import logging
from pathlib import Path

from theloop.adapters.base import RuntimeCheckResult, TaskAdapter
from theloop.renderer import Renderer

log = logging.getLogger(__name__)

_README = """\
# Generic task workspace

theloop has not opinionated this workspace beyond this README. Read the
spec, then create whatever files the task needs (Python scripts, data,
configs, etc.) using your write/edit tools.

There is no rendered preview for this task type — your work is judged from
the spec plus the text-like files you create. Make sure that final message
tells the judge what you produced and where to find it (e.g. "wrote
`solver.py` with a `solve(input: list[int]) -> int` function; sample run
on the example input returns 42").
"""

_SCAFFOLD_NAMES = {"README.md"}
_IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
_TEXT_SUFFIXES = {
    ".cfg",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsonl",
    ".md",
    ".markdown",
    ".py",
    ".rst",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}


class GenericAdapter(TaskAdapter):
    name = "generic"
    has_visual_artifact = False

    def prepare(self, workspace: Path) -> None:
        (workspace / "README.md").write_text(_README)
        log.debug("generic scaffold written to %s", workspace)

    def runtime_check(self, workspace: Path) -> RuntimeCheckResult:
        if not workspace.exists():
            return RuntimeCheckResult(ok=False, log="workspace does not exist")
        files = [
            p for p in workspace.rglob("*")
            if p.is_file() and ".git" not in p.parts and p.name != "README.md"
        ]
        if not files:
            return RuntimeCheckResult(
                ok=False,
                log="workspace contains no files beyond README.md — pi produced nothing",
            )
        return RuntimeCheckResult(ok=True, log=f"workspace has {len(files)} non-scaffold files")

    async def render(self, workspace: Path, out_png: Path, renderer: Renderer) -> None:
        # Loop never calls this because has_visual_artifact = False, but be
        # explicit so a misuse fails loud.
        raise NotImplementedError("GenericAdapter has no visual artifact")

    def artifact_text(self, workspace: Path) -> str | None:
        """Return text-like files created by pi, labeled by relative path.

        Generic tasks can be prose, scripts, configs, or data. The old
        behavior exposed none of those files to the judge, so text-only runs
        were scored as missing artifacts even after successful writes.
        """
        chunks: list[str] = []
        for path in sorted(workspace.rglob("*")):
            if not path.is_file():
                continue
            if any(part in _IGNORED_DIRS for part in path.parts):
                continue
            rel = path.relative_to(workspace)
            if rel.name in _SCAFFOLD_NAMES:
                continue
            if rel.suffix.lower() not in _TEXT_SUFFIXES:
                continue
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                continue
            lines = text.count("\n") + 1
            chunks.append(
                f"### {rel.as_posix()} ({lines} lines, {len(text)} chars)\n\n"
                f"```\n{text}\n```\n"
            )
        if not chunks:
            return None
        return "\n".join(chunks)


# ── manual smoke test ───────────────────────────────────────────────────────


def _smoke() -> None:
    """Usage: python -m theloop.adapters.generic"""
    import tempfile

    from theloop.workspace import Workspace

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    with tempfile.TemporaryDirectory(prefix="theloop-gen-") as tmp:
        ws = Workspace.create(Path(tmp), slug="gen-smoke")
        adapter = GenericAdapter()
        ws.begin_iteration(0)
        adapter.prepare(ws.workspace_path)

        # Empty: only README → fail
        rc = adapter.runtime_check(ws.workspace_path)
        assert not rc.ok, "empty workspace should fail runtime_check"
        print(f"✓ runtime_check rejects empty: {rc.log}")

        # Add a file → ok
        (ws.workspace_path / "hello.py").write_text('print("hi")\n')
        rc2 = adapter.runtime_check(ws.workspace_path)
        assert rc2.ok, f"populated workspace should pass: {rc2.log}"
        print(f"✓ runtime_check ok: {rc2.log}")

        assert adapter.has_visual_artifact is False
        print("✓ has_visual_artifact = False")

        print("✓ all assertions passed")


if __name__ == "__main__":
    _smoke()
