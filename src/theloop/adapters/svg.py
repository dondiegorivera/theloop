"""SVGAdapter — pi edits `artifact.svg`; we render a centered preview."""

from __future__ import annotations

import logging
from pathlib import Path
from xml.etree import ElementTree as ET

from theloop.adapters.base import RuntimeCheckResult, TaskAdapter
from theloop.renderer import Renderer

log = logging.getLogger(__name__)

_INDEX_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>artifact preview</title>
<style>
  html, body { margin: 0; padding: 0; height: 100%; background: #fff; }
  body { display: flex; align-items: center; justify-content: center; }
  img {
    display: block;
    width: 92vw;
    height: 92vh;
    object-fit: contain;
  }
</style>
</head>
<body>
  <img src="artifact.svg" alt="artifact">
</body>
</html>
"""

_PLACEHOLDER_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect x="0" y="0" width="200" height="200" fill="#f4f4f4"/>
  <text x="100" y="105" text-anchor="middle" font-size="16"
        font-family="sans-serif" fill="#888">edit artifact.svg</text>
</svg>
"""

_README = """\
# SVG task workspace

The rendered artifact lives at `artifact.svg`. For detailed or repetitive
SVGs, edit `generate_artifact.py` and run `python generate_artifact.py`
instead of writing a huge SVG directly. Use direct `artifact.svg` edits only
for small incremental fixes.

Tools available: read, write, edit, bash. The renderer screenshots
`index.html` at 1536×1152 after each iteration.
"""

_GENERATOR_PY = '''"""Generate artifact.svg for this SVG task.

Edit this file for detailed/repetitive drawings, then run:

    python generate_artifact.py

Keep generated output in artifact.svg. Do not write to /tmp or absolute paths.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect x="0" y="0" width="200" height="200" fill="#f4f4f4"/>
  <text x="100" y="105" text-anchor="middle" font-size="16"
        font-family="sans-serif" fill="#888">edit generate_artifact.py</text>
</svg>
"""
    Path("artifact.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
'''


class SVGAdapter(TaskAdapter):
    name = "svg"

    def prepare(self, workspace: Path) -> None:
        (workspace / "index.html").write_text(_INDEX_HTML)
        (workspace / "artifact.svg").write_text(_PLACEHOLDER_SVG)
        (workspace / "generate_artifact.py").write_text(_GENERATOR_PY)
        (workspace / "README.md").write_text(_README)
        log.debug("svg scaffold written to %s", workspace)

    def runtime_check(self, workspace: Path) -> RuntimeCheckResult:
        svg_path = workspace / "artifact.svg"
        if not svg_path.exists():
            return RuntimeCheckResult(ok=False, log="artifact.svg missing")
        try:
            ET.parse(svg_path)
        except ET.ParseError as e:
            return RuntimeCheckResult(ok=False, log=f"artifact.svg parse error: {e}")
        return RuntimeCheckResult(ok=True, log="artifact.svg parses as XML")

    async def render(self, workspace: Path, out_png: Path, renderer: Renderer) -> None:
        url = (workspace / "index.html").as_uri()
        await renderer.screenshot(url, out_png, wait_until="load")

    def artifact_text(self, workspace: Path) -> str | None:
        # The vision encoder is reliable for "does this look like a pelican"
        # and unreliable for "is there actually a frame triangle connecting
        # these two wheels". The source is the opposite. Surfacing the SVG
        # source alongside the render lets the judge cross-check structural
        # claims (counts of <line>/<circle>/<path>, presence of named
        # groups) against what it sees rendered.
        svg = workspace / "artifact.svg"
        if not svg.exists():
            return None
        body = svg.read_text()
        return (
            f"### artifact.svg ({len(body)} chars, {body.count(chr(10)) + 1} lines)\n\n"
            "```xml\n"
            f"{body}\n"
            "```\n"
        )


# ── manual smoke test ───────────────────────────────────────────────────────

async def _smoke() -> None:
    """Usage: python -m theloop.adapters.svg"""
    import tempfile

    from theloop.workspace import Workspace

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    with tempfile.TemporaryDirectory(prefix="theloop-svg-") as tmp:
        ws = Workspace.create(Path(tmp), slug="svg-smoke")
        adapter = SVGAdapter()

        ws.begin_iteration(0)
        adapter.prepare(ws.workspace_path)
        assert (ws.workspace_path / "artifact.svg").exists()
        assert (ws.workspace_path / "index.html").exists()
        print("✓ scaffold written")

        rc = adapter.runtime_check(ws.workspace_path)
        assert rc.ok, f"runtime_check failed on placeholder: {rc.log}"
        print(f"✓ runtime_check ok: {rc.log}")

        out_png = ws.artifact_dir(0) / "render.png"
        async with Renderer() as r:
            await adapter.render(ws.workspace_path, out_png, r)
        size = out_png.stat().st_size
        assert size > 0
        with out_png.open("rb") as f:
            assert f.read(8) == b"\x89PNG\r\n\x1a\n", "not a PNG"
        print(f"✓ rendered {out_png.name} ({size} bytes)")

        # break the SVG, runtime_check should now fail
        (ws.workspace_path / "artifact.svg").write_text("<svg><not-closed>")
        rc_bad = adapter.runtime_check(ws.workspace_path)
        assert not rc_bad.ok, "runtime_check should have failed on broken XML"
        print(f"✓ runtime_check rejects broken XML: {rc_bad.log}")

        # missing artifact.svg also fails
        (ws.workspace_path / "artifact.svg").unlink()
        rc_missing = adapter.runtime_check(ws.workspace_path)
        assert not rc_missing.ok
        print(f"✓ runtime_check rejects missing file: {rc_missing.log}")

        print("✓ all assertions passed")


if __name__ == "__main__":
    import asyncio

    asyncio.run(_smoke())
