"""DocAdapter — iteratively improve a markdown / prose document.

Reads `source:` (required) and `rubric:` (optional) from the spec
frontmatter via `configure()`. The source document is copied into the
workspace as `document.md`; pi is instructed to edit it directly. There is
no rendered preview — the judge runs in text-only mode against the spec
body (which carries the rubric) plus pi's last assistant turn.

Output of a doc run is `runs/<id>/workspace/document.md` plus the per-iter
git branches, so you can diff and merge selectively.
"""

from __future__ import annotations

import logging
import shutil
from pathlib import Path
from typing import Any

from theloop.adapters.base import RuntimeCheckResult, TaskAdapter
from theloop.renderer import Renderer

log = logging.getLogger(__name__)

_README = """\
# Document improvement workspace

The document you should edit lives at `document.md`. The spec describes
the rubric and the kind of improvements wanted; refine the document
*incrementally* — do not rewrite from scratch unless the spec says so.

Tools available: read, write, edit, bash. There is no rendered preview;
the judge scores the markdown text directly against the rubric in the
spec.

End your turn with a one-paragraph summary of *what changed and why* — the
judge sees this alongside the document.
"""


class DocAdapter(TaskAdapter):
    name = "doc"
    has_visual_artifact = False

    def __init__(self) -> None:
        self.source_path: Path | None = None
        self.rubric_path: Path | None = None
        self.context_paths: list[Path] = []
        self.context_notes: str = ""

    # ── frontmatter ingest ────────────────────────────────────────────────

    def configure(self, frontmatter: dict[str, Any], spec_path: Path) -> None:
        src = frontmatter.get("source")
        if not src:
            raise ValueError(
                "doc adapter requires `source:` in spec frontmatter "
                "(path to the document to improve, relative to the spec)"
            )
        self.source_path = (spec_path.parent / str(src)).resolve()
        if not self.source_path.exists():
            raise FileNotFoundError(f"doc source not found: {self.source_path}")

        rubric = frontmatter.get("rubric")
        if rubric:
            self.rubric_path = (spec_path.parent / str(rubric)).resolve()
            if not self.rubric_path.exists():
                raise FileNotFoundError(f"doc rubric not found: {self.rubric_path}")

        # Optional read-only reference material that pi can grep but must
        # not edit. Soft default: no context entries is allowed (theoretical
        # docs don't need them).
        ctx = frontmatter.get("context") or []
        if not isinstance(ctx, list):
            raise ValueError("doc `context:` must be a YAML list of paths")
        for entry in ctx:
            p = (spec_path.parent / str(entry)).resolve()
            if not p.exists():
                raise FileNotFoundError(f"doc context path not found: {p}")
            self.context_paths.append(p)

        self.context_notes = str(frontmatter.get("context_notes") or "").strip()

    # ── adapter API ───────────────────────────────────────────────────────

    def prepare(self, workspace: Path) -> None:
        if self.source_path is None:
            raise RuntimeError("DocAdapter.configure() not called before prepare()")
        target = workspace / "document.md"
        shutil.copyfile(self.source_path, target)
        (workspace / "README.md").write_text(_README)
        if self.rubric_path is not None:
            shutil.copyfile(self.rubric_path, workspace / "rubric.md")

        # Copy context entries to workspace/context/<basename>/. Files keep
        # their name; directories are recursively copied. Pi gets
        # self-contained read-only reference material — no symlinks (those
        # would let pi `rm -rf` through to the user's real tree).
        if self.context_paths:
            ctx_root = workspace / "context"
            ctx_root.mkdir(exist_ok=True)
            manifest_lines = []
            for src in self.context_paths:
                dest = ctx_root / src.name
                if src.is_dir():
                    shutil.copytree(src, dest, dirs_exist_ok=True)
                    n_files = sum(1 for _ in dest.rglob("*") if _.is_file())
                    manifest_lines.append(f"- {src.name}/  ({n_files} files, recursive)")
                else:
                    shutil.copyfile(src, dest)
                    manifest_lines.append(f"- {src.name}  ({dest.stat().st_size}B)")
            (ctx_root / "MANIFEST.txt").write_text(
                "Read-only reference material. Do not edit anything in this directory.\n\n"
                + "\n".join(manifest_lines)
                + "\n"
            )

        log.debug(
            "doc scaffold: copied %s → %s%s, context=%d entries",
            self.source_path,
            target,
            f" (+ rubric {self.rubric_path})" if self.rubric_path else "",
            len(self.context_paths),
        )

    def extra_director_notes(self) -> str:
        """Adapter-specific notes the CLI should append to the director's
        adapter_notes for *this run*. Includes context manifest + any
        author-supplied `context_notes` from the spec frontmatter.
        """
        parts: list[str] = []
        if self.context_paths:
            entries = "\n".join(f"  - context/{p.name}" for p in self.context_paths)
            parts.append(
                "READ-ONLY reference material has been placed in `context/`. "
                "Before writing any factual claim (URLs, paths, function "
                "signatures, version numbers, behavior), grep `context/` "
                "and use what you find. If `context/` does not support a "
                "claim you were going to make, do not invent it — keep the "
                "wording abstract or omit the claim. Do NOT edit anything "
                f"under `context/`.\n\nAvailable context:\n{entries}"
            )
        if self.context_notes:
            parts.append("Task-specific context notes:\n" + self.context_notes)
        return "\n\n".join(parts)

    def runtime_check(self, workspace: Path) -> RuntimeCheckResult:
        doc = workspace / "document.md"
        if not doc.exists():
            return RuntimeCheckResult(ok=False, log="document.md missing")
        text = doc.read_text()
        if not text.strip():
            return RuntimeCheckResult(ok=False, log="document.md is empty")
        # Cheap structural pass only. Real markdown frequently has stray
        # backticks inside indented or HTML blocks, so don't try to balance
        # fences — that's the judge's job.
        n_lines = text.count("\n") + 1
        return RuntimeCheckResult(
            ok=True,
            log=f"document.md ok ({len(text)} chars, {n_lines} lines)",
        )

    async def render(self, workspace: Path, out_png: Path, renderer: Renderer) -> None:
        # Loop never calls this because has_visual_artifact = False.
        raise NotImplementedError("DocAdapter has no visual artifact")

    def artifact_text(self, workspace: Path) -> str | None:
        """Return the original + current document, labeled.

        The judge needs both: it scores *improvement against the source*,
        not just rubric-fit on whatever shape the current doc happens to
        have. Without the original visible, pi can rewrite the document
        from scratch and the judge will happily score 1.0 because the
        rewrite ticks every rubric box — but real content has been lost.
        """
        doc = workspace / "document.md"
        if not doc.exists():
            return None
        current = doc.read_text()
        if self.source_path is None or not self.source_path.exists():
            return current
        original = self.source_path.read_text()
        orig_lines = original.count("\n") + 1
        cur_lines = current.count("\n") + 1
        return (
            f"### Original document ({orig_lines} lines, {len(original)} chars)\n\n"
            f"{original}\n\n"
            f"---\n\n"
            f"### Current document ({cur_lines} lines, {len(current)} chars)\n\n"
            f"{current}\n\n"
            f"---\n\n"
            "**How to score:** the spec asks the coder to *improve* the original "
            "document. Score whether the current document is a real improvement "
            "over the original against the spec's rubric. Reward surgical fixes "
            "to specific rubric defects. Penalize regressions: lost content, "
            "weakened claims, removed sections, structural rewrites that "
            "destroy information even if the result looks cleaner. A doc that "
            "shrinks substantially (e.g. >20% line count) without an explicit "
            "request to do so is almost always regressing, not improving."
        )


# ── manual smoke test ───────────────────────────────────────────────────────


def _smoke() -> None:
    """Usage: python -m theloop.adapters.doc"""
    import tempfile

    from theloop.workspace import Workspace

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    with tempfile.TemporaryDirectory(prefix="theloop-doc-") as tmp:
        tmp_path = Path(tmp)
        # Fake source document next to a fake spec path.
        spec_path = tmp_path / "spec.md"
        spec_path.write_text("---\nadapter: doc\nsource: src.md\n---\nimprove src.md\n")
        (tmp_path / "src.md").write_text("# Hello\n\nThis is the original document.\n")

        ws = Workspace.create(tmp_path / "runs", slug="doc-smoke")
        adapter = DocAdapter()
        adapter.configure({"source": "src.md"}, spec_path)
        ws.begin_iteration(0)
        adapter.prepare(ws.workspace_path)

        rc = adapter.runtime_check(ws.workspace_path)
        assert rc.ok, f"runtime_check failed: {rc.log}"
        print(f"✓ runtime_check ok: {rc.log}")

        # Empty document → fail
        (ws.workspace_path / "document.md").write_text("")
        rc_bad = adapter.runtime_check(ws.workspace_path)
        assert not rc_bad.ok
        print(f"✓ runtime_check rejects empty: {rc_bad.log}")

        # Missing source → configure raises
        bad_adapter = DocAdapter()
        try:
            bad_adapter.configure({}, spec_path)
        except ValueError as e:
            print(f"✓ configure rejects missing source: {e}")
        else:
            raise AssertionError("expected ValueError")

        print("✓ all assertions passed")


if __name__ == "__main__":
    _smoke()
