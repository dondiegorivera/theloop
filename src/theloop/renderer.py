"""Headless Chromium screenshot wrapper for visual feedback.

Used by `svg` and `web` adapters to turn an in-workspace HTML page (or SVG
embedded in HTML) into a PNG that the judge can score.

The renderer is an async context manager: launch the browser once per loop
run, render N pages, close. Each `screenshot()` opens a fresh browser context
+ page so iterations don't leak state (cookies, localStorage, console errors)
into each other.
"""

from __future__ import annotations

import logging
from pathlib import Path
from types import TracebackType
from typing import Self

from playwright.async_api import (
    Browser,
    Playwright,
    async_playwright,
)

log = logging.getLogger(__name__)

# 1536×1152 = 1.5× the prior 1024×768. The vision encoder needs enough
# pixels to verify structural detail (e.g. 60 minute ticks on a 600px-viewBox
# watch were sub-pixel-noisy at 1024 — the describe pass kept marking them
# MISSING even when the source had them).
DEFAULT_VIEWPORT = (1536, 1152)


class RendererError(RuntimeError):
    pass


class Renderer:
    def __init__(
        self,
        viewport: tuple[int, int] = DEFAULT_VIEWPORT,
        timeout_s: float = 5.0,
    ) -> None:
        self.viewport = viewport
        self.timeout_s = timeout_s
        self._pw: Playwright | None = None
        self._browser: Browser | None = None

    async def __aenter__(self) -> Self:
        self._pw = await async_playwright().start()
        self._browser = await self._pw.chromium.launch(headless=True)
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        if self._browser:
            await self._browser.close()
            self._browser = None
        if self._pw:
            await self._pw.stop()
            self._pw = None

    async def screenshot(
        self,
        url: str,
        out_png: Path,
        *,
        viewport: tuple[int, int] | None = None,
        wait_until: str = "load",
        wait_for_js: str | None = None,
        timeout_s: float | None = None,
    ) -> None:
        """Navigate to `url` and write a PNG screenshot to `out_png`.

        - `wait_until`: one of "load" | "domcontentloaded" | "networkidle".
        - `wait_for_js`: JS expression to await after navigation, e.g.
          "window.__ready === true" for app-ready signalling.
        - `timeout_s`: overall budget for navigation + wait_for_js.
        """
        if self._browser is None:
            raise RendererError("Renderer used outside of `async with` block")

        vp_w, vp_h = viewport or self.viewport
        timeout_ms = int((timeout_s or self.timeout_s) * 1000)

        out_png.parent.mkdir(parents=True, exist_ok=True)

        ctx = await self._browser.new_context(viewport={"width": vp_w, "height": vp_h})
        try:
            page = await ctx.new_page()
            console_errors: list[str] = []
            page.on("pageerror", lambda e: console_errors.append(str(e)))
            page.on(
                "console",
                lambda m: console_errors.append(f"[{m.type}] {m.text}")
                if m.type == "error"
                else None,
            )
            await page.goto(url, wait_until=wait_until, timeout=timeout_ms)
            if wait_for_js:
                await page.wait_for_function(wait_for_js, timeout=timeout_ms)
            await page.screenshot(path=str(out_png), full_page=False)
            if console_errors:
                log.warning("page console errors during render: %s", console_errors[:5])
        finally:
            await ctx.close()


# ── manual smoke test ───────────────────────────────────────────────────────

async def _smoke() -> None:
    """Usage: python -m theloop.renderer"""
    import asyncio  # noqa: F401  (re-imported for clarity in the smoke entry)
    import tempfile

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    html = """<!doctype html>
<html><body style="margin:0;background:#222;color:#0ff;font-family:sans-serif">
<svg viewBox="0 0 200 80" width="200" height="80">
  <rect x="0" y="0" width="200" height="80" fill="#0ff"/>
  <text x="20" y="50" font-size="32" fill="#222">PONG</text>
</svg>
</body></html>"""

    with tempfile.TemporaryDirectory(prefix="theloop-render-") as tmp:
        tmp_path = Path(tmp)
        page_html = tmp_path / "index.html"
        page_html.write_text(html)
        out_png = tmp_path / "out.png"

        async with Renderer() as r:
            await r.screenshot(page_html.as_uri(), out_png)

        size = out_png.stat().st_size
        assert size > 0, "screenshot is empty"
        # PNG magic bytes
        with out_png.open("rb") as f:
            assert f.read(8) == b"\x89PNG\r\n\x1a\n", "not a PNG"
        print(f"✓ rendered {out_png.name} ({size} bytes)")


if __name__ == "__main__":
    import asyncio

    asyncio.run(_smoke())
