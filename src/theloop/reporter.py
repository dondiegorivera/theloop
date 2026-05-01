"""Reporter — JSONL event log + static HTML index.

The JSONL is the source of truth: one object per loop event,
`{ts, iter, kind, payload}`, append-only. Every component in the loop calls
`reporter.emit(...)`; nothing else writes to it.

`build_html_report(run_dir)` reads back the JSONL, walks `artifacts/iter-N/`
for screenshots, calls `git diff` for each iteration's branch, and writes a
self-contained `index.html` plus per-iter `diff.txt` files. No template
engine — just an f-string-built page.
"""

from __future__ import annotations

import html
import json
import logging
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)


class Reporter:
    def __init__(self, run_dir: Path) -> None:
        self.run_dir = run_dir
        self.events_path = run_dir / "events.jsonl"
        run_dir.mkdir(parents=True, exist_ok=True)
        # Truncate on construction so reruns of the same run_id start clean.
        self.events_path.write_text("")
        self._fh = self.events_path.open("a", buffering=1)  # line-buffered

    def emit(self, kind: str, *, iter: int | None = None, **payload: Any) -> None:
        ev = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "iter": iter,
            "kind": kind,
            "payload": payload,
        }
        self._fh.write(json.dumps(ev, default=_json_default) + "\n")

    def close(self) -> None:
        try:
            self._fh.close()
        except Exception:
            pass

    def __enter__(self) -> "Reporter":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


def _json_default(o: Any) -> Any:
    # Be liberal: paths, dataclasses-as-dicts via __dict__, fall back to str.
    if isinstance(o, Path):
        return str(o)
    if hasattr(o, "__dataclass_fields__"):
        return {k: getattr(o, k) for k in o.__dataclass_fields__}
    return str(o)


# ── HTML report ──────────────────────────────────────────────────────────────


def build_html_report(run_dir: Path) -> Path:
    """Read events.jsonl in `run_dir`, write `index.html` + per-iter diffs.

    Returns the path to the generated index.html. Safe to re-run; overwrites.
    """
    events_path = run_dir / "events.jsonl"
    if not events_path.exists():
        raise FileNotFoundError(f"no events.jsonl at {events_path}")

    events = [json.loads(line) for line in events_path.read_text().splitlines() if line.strip()]
    by_iter: dict[int, dict[str, Any]] = defaultdict(dict)
    run_meta: dict[str, Any] = {}
    run_end: dict[str, Any] = {}

    for ev in events:
        kind = ev.get("kind")
        it = ev.get("iter")
        payload = ev.get("payload") or {}
        if kind == "run_start":
            run_meta = payload | {"ts": ev.get("ts")}
        elif kind == "run_end":
            run_end = payload | {"ts": ev.get("ts")}
        elif it is not None:
            by_iter[it][kind] = payload

    # Per-iter git diffs (best effort: workspace must exist + be a repo).
    workspace_path = run_dir / "workspace"
    diffs: dict[int, str] = {}
    if (workspace_path / ".git").exists():
        try:
            import git
            repo = git.Repo(workspace_path)
            for it in sorted(by_iter):
                base = "main" if it == 0 else f"iter/{it - 1}"
                target = f"iter/{it}"
                try:
                    diffs[it] = repo.git.diff(base, target)
                except Exception as e:
                    log.debug("diff iter %d failed: %s", it, e)
                    diffs[it] = f"(diff unavailable: {e})"
        except Exception as e:
            log.warning("could not open workspace repo for diffs: %s", e)

    # Persist diffs alongside the artifacts dir so the HTML can link them.
    artifacts_root = run_dir / "artifacts"
    for it, diff_text in diffs.items():
        d = artifacts_root / f"iter-{it}"
        d.mkdir(parents=True, exist_ok=True)
        (d / "diff.txt").write_text(diff_text or "(empty diff)")

    spec_text: str | None = None
    spec_path = run_dir / "spec.md"
    if spec_path.exists():
        try:
            spec_text = spec_path.read_text()
        except Exception as e:
            log.debug("could not read original spec for header: %s", e)

    out_path = run_dir / "index.html"
    out_path.write_text(
        _render_html(run_dir.name, run_meta, run_end, by_iter, diffs, spec_text)
    )
    log.info("wrote report: %s", out_path)
    return out_path


def _render_html(
    run_id: str,
    run_meta: dict[str, Any],
    run_end: dict[str, Any],
    by_iter: dict[int, dict[str, Any]],
    diffs: dict[int, str],
    spec_text: str | None = None,
) -> str:
    cards = "\n".join(_render_iter_card(i, by_iter[i], diffs.get(i, "")) for i in sorted(by_iter))

    summary_pairs = [
        ("adapter", run_meta.get("adapter", "?")),
        ("max iters", run_meta.get("max_iters", "?")),
        ("threshold", run_meta.get("score_threshold", "?")),
        ("plateau window", run_meta.get("no_improvement_for", "?")),
        ("stop reason", run_end.get("reason", "—")),
        ("best score", _fmt_score(run_end.get("best_score"))),
        ("iters run", run_end.get("iters_run", len(by_iter))),
        ("started", run_meta.get("ts", "?")),
        ("ended", run_end.get("ts", "—")),
    ]
    summary_rows = "".join(
        f"<tr><th>{html.escape(str(k))}</th><td>{html.escape(str(v))}</td></tr>"
        for k, v in summary_pairs
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>theloop — {html.escape(run_id)}</title>
<style>
  :root {{
    --bg: #0f1115; --card: #1a1d23; --fg: #e6e6e6; --muted: #9aa0aa;
    --accent: #6cf; --good: #7c7; --bad: #f88;
  }}
  html, body {{ background: var(--bg); color: var(--fg); margin: 0;
    font: 14px/1.5 -apple-system, system-ui, "Segoe UI", sans-serif; }}
  header {{ padding: 24px 32px; border-bottom: 1px solid #222; }}
  header h1 {{ margin: 0 0 8px; font-size: 18px; font-weight: 600; }}
  header .id {{ color: var(--muted); font-family: ui-monospace, monospace; }}
  header details {{ margin-top: 16px; max-width: 1200px; }}
  header details summary {{ color: var(--muted); cursor: pointer;
    font-size: 12px; text-transform: uppercase; letter-spacing: 0.04em; }}
  header details summary:hover {{ color: var(--accent); }}
  header details pre {{ background: #0c0e12; color: #ddd;
    padding: 12px 16px; border-radius: 6px; margin-top: 8px;
    font-family: ui-monospace, monospace; font-size: 12px;
    overflow: auto; max-height: 400px; white-space: pre-wrap; }}
  main {{ padding: 24px 32px 64px; max-width: 1200px; margin: 0 auto; }}
  section.summary table {{ border-collapse: collapse; margin-bottom: 32px; }}
  section.summary th, section.summary td {{
    padding: 4px 12px 4px 0; text-align: left; vertical-align: top;
  }}
  section.summary th {{ color: var(--muted); font-weight: 400; }}
  .card {{ background: var(--card); border-radius: 8px; padding: 20px;
    margin-bottom: 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }}
  .card .meta h2 {{ margin: 0 0 12px; font-size: 16px; }}
  .card .score {{ font-family: ui-monospace, monospace; font-size: 18px; }}
  .card .score.good {{ color: var(--good); }}
  .card .score.bad {{ color: var(--bad); }}
  .card .label {{ color: var(--muted); font-size: 12px;
    text-transform: uppercase; letter-spacing: 0.04em; margin-top: 16px; }}
  .card pre {{ background: #0c0e12; color: #ddd; padding: 12px; border-radius: 6px;
    overflow: auto; max-height: 300px; font-size: 12px; }}
  .card img {{ max-width: 100%; border-radius: 6px; background: #fff; }}
  .card .render-missing {{ color: var(--muted); font-style: italic; }}
  .card a {{ color: var(--accent); }}
  .pill {{ display: inline-block; padding: 2px 8px; border-radius: 12px;
    font-size: 11px; background: #2a2e36; color: var(--muted); margin-left: 6px; }}
  .pill.ok {{ background: #1d3a1f; color: #9eda9e; }}
  .pill.bad {{ background: #3a1d1d; color: #da9e9e; }}
</style>
</head>
<body>
<header>
  <h1>theloop run</h1>
  <div class="id">{html.escape(run_id)}</div>
  {_render_spec_block(spec_text)}
</header>
<main>
  <section class="summary">
    <table>{summary_rows}</table>
  </section>
  {cards}
</main>
</body>
</html>
"""


def _render_spec_block(spec_text: str | None) -> str:
    if not spec_text:
        return ""
    return (
        "<details>"
        "<summary>original spec</summary>"
        f"<pre>{html.escape(spec_text)}</pre>"
        "</details>"
    )


def _render_iter_card(it: int, ev: dict[str, Any], diff_text: str) -> str:
    plan_end = ev.get("plan_end") or {}
    rc = ev.get("runtime_check") or {}
    render = ev.get("render") or {}
    judge_end = ev.get("judge_end") or {}
    commit = ev.get("commit") or {}
    pi_end = ev.get("pi_end") or {}

    intent = plan_end.get("intent", "(no intent)")
    score = judge_end.get("score")
    critique = judge_end.get("critique", "(no critique)")
    done = judge_end.get("done", False)
    rc_ok = bool(rc.get("ok"))
    rc_log = rc.get("log", "")
    sha = commit.get("sha")
    branch = commit.get("branch")
    png_rel = render.get("png")  # absolute path; relativize for HTML
    if png_rel:
        # png is absolute; build relative-to-run-dir for HTML
        # render_dir is run_dir/artifacts/iter-N/render.png — last 3 parts.
        png_rel = "/".join(Path(png_rel).parts[-3:])

    score_class = ""
    score_str = "—"
    if score is not None:
        score_str = f"{score:.2f}"
        score_class = "good" if score >= 0.8 else ("bad" if score < 0.4 else "")

    pills = []
    pills.append(f'<span class="pill {"ok" if rc_ok else "bad"}">runtime {"ok" if rc_ok else "fail"}</span>')
    if done:
        pills.append('<span class="pill ok">done</span>')
    if pi_end.get("touched"):
        pills.append(f'<span class="pill">touched {len(pi_end["touched"])}</span>')

    diff_link = ""
    if diff_text:
        diff_link = f'<a href="artifacts/iter-{it}/diff.txt">view diff</a>'
        if branch:
            diff_link = f"{branch}: {diff_link}"
        if sha:
            diff_link += f' <code>{html.escape(sha[:8])}</code>'

    img_html = (
        f'<img src="{html.escape(png_rel)}" alt="iter {it} render">'
        if png_rel
        else '<div class="render-missing">(no render — runtime check failed or non-visual adapter)</div>'
    )

    return f"""
  <article class="card">
    <div class="render">{img_html}</div>
    <div class="meta">
      <h2>iter {it} <span class="score {score_class}">{score_str}</span> {''.join(pills)}</h2>

      <div class="label">intent</div>
      <div>{html.escape(intent)}</div>

      <div class="label">judge critique</div>
      <div>{html.escape(critique)}</div>

      <div class="label">runtime check</div>
      <div>{html.escape(rc_log)}</div>

      <div class="label">commit</div>
      <div>{diff_link or "(no commit)"}</div>
    </div>
  </article>
"""


def _fmt_score(v: Any) -> str:
    if v is None:
        return "—"
    try:
        return f"{float(v):.2f}"
    except (TypeError, ValueError):
        return str(v)


# ── manual smoke test ───────────────────────────────────────────────────────


def _smoke() -> None:
    """Usage: python -m theloop.reporter"""
    import tempfile

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    with tempfile.TemporaryDirectory(prefix="theloop-rep-") as tmp:
        rep = Reporter(Path(tmp))
        rep.emit("run_start", spec_path="examples/pelican.spec.md")
        rep.emit("plan_start", iter=0)
        rep.emit("plan_end", iter=0, intent="initial sketch")
        rep.emit("judge", iter=0, score=0.4, critique="needs beak", done=False)
        rep.emit("run_end", reason="max_iters", best_score=0.4)
        rep.close()

        lines = rep.events_path.read_text().splitlines()
        print(f"✓ wrote {len(lines)} events")
        for line in lines:
            obj = json.loads(line)
            print(f"  iter={obj['iter']} kind={obj['kind']} payload={obj['payload']}")
        assert len(lines) == 5


if __name__ == "__main__":
    _smoke()
