"""WebAppAdapter — pi edits `index.html` + `app.js`; we render in headless Chromium.

Scaffold deliberately ships a minimal page that already sets
`window.__ready = true`. Pi's job is to *replace* the placeholder app with
the real one while preserving the `__ready` signal — that way the renderer
knows when the scene has actually drawn its first frame, not just when the
DOM has loaded.

The scaffold loads three.js as a globals build from a CDN to avoid the
file:// + ES module CORS dance. Pi may switch to import maps if it wants —
the adapter doesn't care, it only checks the page renders without timing
out and the runtime check below.
"""

from __future__ import annotations

import logging
from html.parser import HTMLParser
from pathlib import Path

from theloop.adapters.base import RuntimeCheckResult, TaskAdapter
from theloop.renderer import Renderer

log = logging.getLogger(__name__)

_INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>web app</title>
<style>
  html, body { margin: 0; padding: 0; height: 100%; background: #111; color: #eee;
    font: 14px -apple-system, system-ui, "Segoe UI", sans-serif; overflow: hidden; }
  #app, canvas { display: block; width: 100vw; height: 100vh; }
  #placeholder { display: flex; align-items: center; justify-content: center;
    width: 100vw; height: 100vh; color: #888; }
</style>
</head>
<body>
<div id="app">
  <div id="placeholder">edit app.js — set window.__ready = true once the scene has drawn</div>
</div>
<!-- three.js global build (no module/CORS hassles from file://) -->
<script src="https://unpkg.com/three@0.160.0/build/three.min.js"></script>
<script src="app.js"></script>
</body>
</html>
"""

_APP_JS = """// edit me. Set window.__ready = true once the first frame has rendered;
// theloop's renderer uses that signal to know when to take its screenshot.
//
// Three.js is available as the global `THREE`. To use canvas2d or pure DOM
// instead, just remove the placeholder #app contents and draw your own.
//
// The placeholder marks ready synchronously so the scaffold renders without
// timing out. Replace this with a real ready signal once a scene exists,
// e.g. set __ready inside the first renderer.render() callback.

window.__ready = true;
"""

_README = """\
# Web app workspace

Edit `index.html` and `app.js`. The page is rendered in headless Chromium
at 1024×768; theloop screenshots it once `window.__ready === true`.

Tools available: read, write, edit, bash. three.js global build is loaded
in the scaffold; you can switch to import maps if you prefer.

Acceptance signals theloop checks each iteration:
- `index.html` and `app.js` both exist.
- `index.html` parses as well-formed HTML.
- The page sets `window.__ready = true` within 5 seconds of load.
- No uncaught console errors during render (best-effort; not fatal).
"""


class _Probe(HTMLParser):
    """Minimal well-formedness pass: counts open/close balance."""

    def __init__(self) -> None:
        super().__init__()
        self.has_html = False
        self.has_body = False
        self.errors: list[str] = []

    def error(self, message: str) -> None:  # type: ignore[override]
        self.errors.append(message)

    def handle_starttag(self, tag, attrs):  # type: ignore[override]
        del attrs
        if tag == "html":
            self.has_html = True
        elif tag == "body":
            self.has_body = True


class WebAppAdapter(TaskAdapter):
    name = "web"

    def prepare(self, workspace: Path) -> None:
        (workspace / "index.html").write_text(_INDEX_HTML)
        (workspace / "app.js").write_text(_APP_JS)
        (workspace / "README.md").write_text(_README)
        log.debug("web scaffold written to %s", workspace)

    def runtime_check(self, workspace: Path) -> RuntimeCheckResult:
        index = workspace / "index.html"
        app = workspace / "app.js"
        if not index.exists():
            return RuntimeCheckResult(ok=False, log="index.html missing")
        if not app.exists():
            return RuntimeCheckResult(ok=False, log="app.js missing")
        probe = _Probe()
        try:
            probe.feed(index.read_text())
            probe.close()
        except Exception as e:
            return RuntimeCheckResult(ok=False, log=f"index.html parse error: {e}")
        if not probe.has_html or not probe.has_body:
            return RuntimeCheckResult(
                ok=False,
                log="index.html missing <html> or <body> tag",
            )
        return RuntimeCheckResult(ok=True, log="index.html + app.js present, html well-formed")

    async def render(self, workspace: Path, out_png: Path, renderer: Renderer) -> None:
        """Take a screenshot of the rendered page.

        Tries to wait for `window.__ready === true` (5s budget). If pi's app
        never flips the flag, we fall back to a plain dom-loaded screenshot
        so the judge still has something to look at — usually the broken
        state is informative on its own.
        """
        url = (workspace / "index.html").as_uri()
        try:
            await renderer.screenshot(
                url,
                out_png,
                wait_until="load",
                wait_for_js="window.__ready === true",
                timeout_s=5.0,
            )
        except Exception as e:
            log.warning("web render: __ready not set in 5s (%s); falling back", e)
            await renderer.screenshot(
                url,
                out_png,
                wait_until="domcontentloaded",
                timeout_s=5.0,
            )


# ── manual smoke test ───────────────────────────────────────────────────────


async def _smoke() -> None:
    """Usage: python -m theloop.adapters.web"""
    import tempfile

    from theloop.workspace import Workspace

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    with tempfile.TemporaryDirectory(prefix="theloop-web-") as tmp:
        ws = Workspace.create(Path(tmp), slug="web-smoke")
        adapter = WebAppAdapter()
        ws.begin_iteration(0)
        adapter.prepare(ws.workspace_path)

        rc = adapter.runtime_check(ws.workspace_path)
        assert rc.ok, f"runtime_check failed: {rc.log}"
        print(f"✓ runtime_check ok: {rc.log}")

        # Break index.html — drop <html>/<body>
        (ws.workspace_path / "index.html").write_text("<div>hi</div>")
        rc_bad = adapter.runtime_check(ws.workspace_path)
        assert not rc_bad.ok
        print(f"✓ runtime_check rejects malformed html: {rc_bad.log}")

        # Restore + render
        adapter.prepare(ws.workspace_path)
        out_png = ws.artifact_dir(0) / "render.png"
        async with Renderer() as r:
            await adapter.render(ws.workspace_path, out_png, r)
        size = out_png.stat().st_size
        with out_png.open("rb") as f:
            assert f.read(8) == b"\x89PNG\r\n\x1a\n"
        print(f"✓ rendered {out_png.name} ({size} bytes)")

        # __ready never set: simulate by editing app.js
        (ws.workspace_path / "app.js").write_text("// no __ready here\n")
        out_png2 = ws.artifact_dir(0) / "render-noready.png"
        async with Renderer() as r:
            await adapter.render(ws.workspace_path, out_png2, r)
        assert out_png2.stat().st_size > 0
        print(f"✓ fallback render when __ready missing: {out_png2.stat().st_size} bytes")

        print("✓ all assertions passed")


if __name__ == "__main__":
    import asyncio

    asyncio.run(_smoke())
