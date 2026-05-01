"""Typer CLI: `python -m theloop run <spec.md>`.

Reads optional YAML frontmatter from the spec, instantiates every component,
and hands off to `Loop.run()`. The CLI is the only place that knows how to
wire the pieces together — `Loop` itself takes them as constructor args.
"""

from __future__ import annotations

import asyncio
import logging
import re
from pathlib import Path
from typing import Annotated, Any

import typer
import yaml

from theloop.adapters import get_adapter
from theloop.judge import Judge
from theloop.loop import Loop
from theloop.models import Hat, alias_for
from theloop.orchestrator import Orchestrator
from theloop.pi_client import PiClient
from theloop.renderer import Renderer
from theloop.reporter import Reporter, build_html_report
from theloop.terminator import TerminationConfig, Terminator
from theloop.workspace import Workspace, make_run_id

log = logging.getLogger(__name__)

app = typer.Typer(add_completion=False, no_args_is_help=True)

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_BLANK_LINES_RE = re.compile(r"\n{3,}")

# Default per-adapter pi guidance. Loop hands this string to the director
# verbatim so it knows which file pi should edit and how.
_PATH_RULE = (
    "Use **relative paths only** in `read` / `write` / `edit` / `create` calls "
    "and inside `bash` commands (e.g. `artifact.svg`, not "
    "`/abs/path/artifact.svg`). Your working directory IS the workspace root — "
    "do not construct absolute paths and do not `cd` to `/src/...`."
)

_ADAPTER_NOTES: dict[str, str] = {
    "svg": (
        "Primary output is `artifact.svg`. Do not touch `index.html` or "
        "`README.md`. For a new detailed/repetitive SVG, edit the relative "
        "workspace helper `generate_artifact.py` and run "
        "`python generate_artifact.py`; do not attempt a giant one-shot "
        "`artifact.svg` write. Direct `artifact.svg` edits are only for small "
        "incremental fixes. If pi thinks a file was truncated, it must switch "
        "to `generate_artifact.py`, not retry the same huge write. Never write "
        "helper files under `/tmp` or any absolute path. On later iterations, "
        "do not read all of `artifact.svg`; it is generated output and can be "
        "large. Inspect/edit `generate_artifact.py`, then run it and use small "
        "`grep`/XML checks against `artifact.svg`. On fix iterations, do not "
        "read full generated files. Use `rg`, `sed -n`, or `read` with small "
        "`offset`/`limit` windows to inspect only the relevant generator "
        "section before editing. On fix iterations, make the edit promptly: "
        "at most one locating `rg`/`grep` command before `edit`, no broad "
        "inspection phase. The SVG must parse as XML; close every tag "
        "and quote every attribute. Do not install packages or generate "
        "preview PNGs; the loop renderer creates screenshots after pi exits. "
        f"{_PATH_RULE}"
    ),
    "web": (
        "Edit `index.html` and `app.js` (and add JS/CSS files as needed). "
        "Three.js is loaded as a global `THREE` from a CDN — you may switch "
        "to import maps if you prefer. The page MUST set "
        "`window.__ready = true` once the first frame has rendered, "
        "otherwise the renderer falls back to a dom-loaded screenshot. "
        "Avoid uncaught console errors. The page is captured at 1536×1152. "
        f"{_PATH_RULE}"
    ),
    "generic": (
        "Create whatever files the spec requires (Python scripts, data, "
        "configs, etc.). There is no rendered preview — the judge scores "
        "from the spec plus your final assistant message. End your turn "
        "with a clear summary of what you produced and where to find it. "
        f"{_PATH_RULE}"
    ),
    "doc": (
        "Edit `document.md` directly — it is already populated with the "
        "source document. **REFINE INCREMENTALLY.** Do not rewrite from "
        "scratch. Do not `write_file` the entire document with a new "
        "shorter version — that is a regression, not an improvement, and "
        "the judge will penalize it. Use `edit` to make surgical changes "
        "to specific lines, sections, or paragraphs. If the source is "
        "523 lines and you produce 252, you have destroyed information. "
        "The judge scores improvement *over the original* against the "
        "rubric in the spec; lost content counts against you even if "
        "the result looks cleaner. End your turn with a one-paragraph "
        "summary of what you changed and why. "
        f"{_PATH_RULE}"
    ),
}


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return fm, body


def _normalize_spec_text(text: str) -> str:
    """Compact markdown specs before sending them through every agent turn."""
    lines: list[str] = []
    in_fence = False
    for raw_line in text.replace("\t", " ").replace("\u00a0", " ").splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            lines.append(raw_line.rstrip())
            continue
        if in_fence:
            lines.append(raw_line.rstrip())
        elif stripped:
            lines.append(" ".join(stripped.split()))
        else:
            lines.append("")
    compact = _BLANK_LINES_RE.sub("\n\n", "\n".join(lines)).strip()
    return compact + "\n" if compact else ""


def _pi_alias_for_adapter(adapter_name: str) -> str:
    # Pi is on the hot path every iteration. Use the CODER hat for enough
    # output budget; the CLI's default --pi-thinking=off keeps it from spending
    # that budget on reasoning instead of edits.
    return alias_for(Hat.CODER)


@app.command()
def run(
    spec_path: Annotated[Path, typer.Argument(help="Path to the spec markdown file.")],
    adapter: Annotated[str | None, typer.Option(help="Override frontmatter `adapter`.")] = None,
    max_iters: Annotated[int | None, typer.Option(help="Override frontmatter `max_iters`.")] = None,
    threshold: Annotated[float | None, typer.Option(help="Override `score_threshold`.")] = None,
    no_improvement_for: Annotated[int | None, typer.Option(help="Plateau window.")] = None,
    runs_dir: Annotated[Path, typer.Option(help="Where to put runs/.")] = Path("runs"),
    run_id: Annotated[str | None, typer.Option(help="Override the auto-generated run id.")] = None,
    pi_timeout_s: Annotated[float, typer.Option(help="Per-iteration pi timeout.")] = 600.0,
    pi_no_write_timeout_s: Annotated[
        float,
        typer.Option(
            help=(
                "Abort a pi turn if it has not called write/edit/create within "
                "this many seconds. Set 0 to disable."
            )
        ),
    ] = 120.0,
    pi_thinking: Annotated[
        str | None,
        typer.Option(
            help=(
                "Optional pi thinking level override: off, minimal, low, medium, "
                "high, xhigh. Defaults to off for faster tool use."
            )
        ),
    ] = "off",
    pi_no_session: Annotated[
        bool,
        typer.Option(help="Launch pi with --no-session for ephemeral sessions."),
    ] = False,
    log_level: Annotated[str, typer.Option(help="Python logging level.")] = "INFO",
) -> None:
    """Run a closed agentic loop against a spec."""
    logging.basicConfig(
        level=log_level.upper(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    # Httpx logs every request at INFO; quiet it unless the user opts in.
    if log_level.upper() != "DEBUG":
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("openai").setLevel(logging.WARNING)

    text = spec_path.read_text()
    frontmatter, _body = _parse_frontmatter(text)
    spec_text = _normalize_spec_text(text)

    adapter_name = adapter or frontmatter.get("adapter")
    if not adapter_name:
        raise typer.BadParameter(
            "no `adapter` in frontmatter and --adapter not provided"
        )

    cfg = TerminationConfig(
        max_iters=max_iters or frontmatter.get("max_iters", 10),
        score_threshold=threshold or frontmatter.get("score_threshold", 0.85),
        no_improvement_for=no_improvement_for or frontmatter.get("no_improvement_for", 3),
    )

    slug = spec_path.stem
    rid = run_id or make_run_id(slug)
    asyncio.run(
        _run_loop(
            spec_text=spec_text,
            spec_path=spec_path.resolve(),
            frontmatter=frontmatter,
            adapter_name=adapter_name,
            adapter_notes=_ADAPTER_NOTES.get(adapter_name, ""),
            cfg=cfg,
            runs_dir=runs_dir,
            run_id=rid,
            pi_timeout_s=pi_timeout_s,
            pi_no_write_timeout_s=pi_no_write_timeout_s,
            pi_thinking=pi_thinking,
            pi_no_session=pi_no_session,
        )
    )


async def _run_loop(
    spec_text: str,
    spec_path: Path,
    frontmatter: dict[str, Any],
    adapter_name: str,
    adapter_notes: str,
    cfg: TerminationConfig,
    runs_dir: Path,
    run_id: str,
    pi_timeout_s: float,
    pi_no_write_timeout_s: float,
    pi_thinking: str | None,
    pi_no_session: bool,
) -> None:
    workspace = Workspace.create(runs_dir, run_id=run_id)
    adapter = get_adapter(adapter_name)
    adapter.configure(frontmatter, spec_path)
    extra = adapter.extra_director_notes()
    if extra:
        adapter_notes = (adapter_notes + "\n\n" + extra).strip()
    pi_alias = _pi_alias_for_adapter(adapter_name)

    print(f"run_id:        {run_id}")
    print(f"adapter:       {adapter_name}")
    print(f"max_iters:     {cfg.max_iters}")
    print(f"threshold:     {cfg.score_threshold}")
    print(f"no_improve_for:{cfg.no_improvement_for}")
    print(f"pi model:      {pi_alias}")
    print(f"pi thinking:   {pi_thinking or '(pi default)'}")
    print(f"pi no-session: {pi_no_session}")
    print(f"pi no-write:   {pi_no_write_timeout_s}s")
    print(f"workspace:     {workspace.workspace_path}")

    orchestrator = Orchestrator()
    judge = Judge()
    if adapter.has_visual_artifact:
        await judge.vision_probe()
        print(f"vision:        {'ok' if judge.vision_available else 'unavailable (text-only fallback)'}")
    terminator = Terminator(cfg)

    def pi_factory() -> PiClient:
        return PiClient(
            workspace=workspace.workspace_path,
            model_alias=pi_alias,
            thinking_level=pi_thinking,
            no_session=pi_no_session,
        )

    with Reporter(workspace.run_dir) as reporter:
        if adapter.has_visual_artifact:
            async with Renderer() as renderer:
                loop = Loop(
                    spec=spec_text,
                    adapter=adapter,
                    adapter_notes=adapter_notes,
                    orchestrator=orchestrator,
                    pi_factory=pi_factory,
                    renderer=renderer,
                    judge=judge,
                    terminator=terminator,
                    workspace=workspace,
                    reporter=reporter,
                    pi_timeout_s=pi_timeout_s,
                    pi_no_write_timeout_s=pi_no_write_timeout_s,
                )
                result = await loop.run()
        else:
            loop = Loop(
                spec=spec_text,
                adapter=adapter,
                adapter_notes=adapter_notes,
                orchestrator=orchestrator,
                pi_factory=pi_factory,
                renderer=None,
                judge=judge,
                terminator=terminator,
                workspace=workspace,
                reporter=reporter,
                pi_timeout_s=pi_timeout_s,
                pi_no_write_timeout_s=pi_no_write_timeout_s,
            )
            result = await loop.run()

    print()
    print(f"stop reason:   {result.stop_reason.value}")
    print(f"best score:    {result.best_score}")
    print(f"iterations:    {len(result.iterations)}")
    for r in result.iterations:
        flag = "✓" if r.runtime_check.ok else "✗"
        score = f"{r.verdict.score:.2f}" if r.verdict.score is not None else "  ? "
        print(f"  iter {r.iter}: rc={flag} score={score}  intent={r.intent[:80]}")
    print(f"events:        {workspace.run_dir / 'events.jsonl'}")
    try:
        report_path = build_html_report(workspace.run_dir)
        print(f"report:        {report_path}")
    except Exception as e:
        log.warning("could not build HTML report: %s", e)


@app.command()
def report(
    run_dir: Annotated[Path, typer.Argument(help="Path to a runs/<id> directory.")],
) -> None:
    """Regenerate the static HTML report for an existing run."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    out = build_html_report(run_dir)
    typer.echo(f"wrote {out}")


if __name__ == "__main__":
    app()
