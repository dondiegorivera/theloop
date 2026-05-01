# theloop

A closed agentic loop in the spirit of Karpathy's *autoresearch*, but generic
over artifact type. Given a free-form markdown **spec**, theloop iterates:

> *plan → write code → check → render → judge → revise*

…until a stop condition fires (rubric satisfied, score plateaued, or hard
iteration cap). Each iteration lives on its own git branch in an isolated
per-run workspace, and the whole run is pinned in a static HTML report.

The orchestration is [agno](https://github.com/agno-agi/agno); the code-writer
is [pi](https://github.com/mariozechner/pi-coding-agent) over JSON-RPC stdio;
the only model family is Qwen3.6 served by a local
[LiteLLM](https://github.com/BerriAI/litellm) proxy. Vision feedback is
first-class: the renderer screenshots the artifact and a vision call
participates in scoring.

## What it does today

Four task adapters, all working end-to-end:

| Adapter   | Artifact                       | Render path                   | Judge input            |
| --------- | ------------------------------ | ----------------------------- | ---------------------- |
| `svg`     | `artifact.svg`                 | Chromium screenshot           | image + SVG source     |
| `web`     | `index.html` + JS/CSS          | Chromium screenshot           | image                  |
| `doc`     | `document.md` (refines source) | none                          | original + current text |
| `generic` | whatever the spec asks for     | none                          | spec + assistant turn  |

The judge runs in two passes: an **adversarial describe** classifies every
spec-required element as PRESENT / PARTIAL / HIDDEN / MISSING with concrete
evidence, and a **verdict** call maps those classifications to a JSON
`{score, critique, done}` with explicit ceilings on structural defects. The
two-stage design exists because a single-call judge tends to pattern-match
"a pelican on a bicycle" and rubber-stamp obviously-broken artifacts.

## Quick start

```bash
# 1. Python 3.12 venv with deps
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
playwright install chromium

# 2. Point at a LiteLLM proxy serving the Qwen3.6 aliases
cp .env.example .env  # then edit
# LITELLM_BASE_URL=http://<host>:<port>
# LITELLM_MASTER_KEY=...

# 3. Run a spec
python -m theloop run examples/pelican.spec.md
```

Each run lands in `runs/<id>/` with:

- `events.jsonl` — every plan / direct / pi / runtime / render / judge / commit event
- `index.html` — self-contained report you can open in a browser
- `workspace/` — isolated git working tree, one branch per iteration (`iter/0`, `iter/1`, …)
- `artifacts/iter-N/` — render PNG, judge description, pi prompt, pi assistant text, per-iter spec snapshot

## Spec format

Specs are markdown files with optional YAML frontmatter:

```markdown
---
adapter: svg              # svg | web | doc | generic
max_iters: 10
score_threshold: 0.95
no_improvement_for: 3
---

# Pelican on a bicycle

Draw an SVG of a pelican riding a bicycle. The pelican should be
recognizable... [free-form spec body]
```

`doc` adapter takes additional keys:

```yaml
source: ../docs/spec.md       # file to iteratively improve
context:                       # read-only reference material
  - ../src/theloop
  - ../docs/litellm-endpoints.md
context_notes: |               # task-specific gotchas pi should know
  - The LiteLLM proxy URL is in `.env`; the api_base lines in
    context/litellm-endpoints.md are the upstream endpoints, NOT the proxy.
```

See `examples/` for working specs covering all four adapters.

## CLI

```bash
python -m theloop run <spec.md>
    [--adapter svg|web|doc|generic]   # override frontmatter
    [--max-iters N]                   # override frontmatter
    [--threshold 0.0-1.0]             # override frontmatter
    [--no-improvement-for N]          # plateau window
    [--run-id <slug>]                 # override auto-generated id
    [--pi-timeout-s 600]              # per-iteration pi timeout
    [--log-level INFO|DEBUG|...]

python -m theloop report <runs/<id>>  # rebuild HTML report from events.jsonl
```

## Architecture

```
                 ┌──────────────────┐
                 │   theloop CLI    │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │       Loop       │   one Python process, async
                 │  iter 0 .. N     │
                 └─┬─────┬─────┬──┬─┘
                   │     │     │  │
        ┌──────────▼─┐ ┌─▼──┐ ┌▼─┐ ┌▼─────┐
        │Orchestrator│ │ Pi │ │R │ │Judge │
        │ (agno,     │ │RPC │ │e │ │ 2-   │
        │  planner + │ │stdio│ │n │ │ pass │
        │  director) │ │    │ │d │ │      │
        └──────┬─────┘ └─┬──┘ └─┬┘ └──┬───┘
               │         │      │     │
               └─── Qwen3.6 via LiteLLM proxy ────┘
                          │
                 ┌────────▼─────────┐
                 │   TaskAdapter    │   svg | web | doc | generic
                 │ prepare/render/  │
                 │ runtime_check/   │
                 │ artifact_text    │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │   Workspace      │   git per-iter branches
                 │   Reporter       │   JSONL events + HTML
                 │   Terminator     │   done | threshold | plateau | max_iters
                 └──────────────────┘
```

The Loop owns no LLM state. All persistence goes through `Workspace` (git +
files) and `Reporter` (JSONL events). The CLI is the only place that wires
components together; `Loop` itself takes everything as constructor args, so
unit tests and smoke scripts can swap any piece.

## Model roles

theloop uses **hat-switching**: one alias per role rather than one agent per
task. Aliases are resolved at the LiteLLM proxy, so the underlying model can
be swapped without touching code. The roles:

| Hat            | Default alias                  | Purpose                                                  |
| -------------- | ------------------------------ | -------------------------------------------------------- |
| `PLANNER`      | `Qwen3.6-Mesh-Thinking-Long`   | Refine spec + emit iteration intent                      |
| `DIRECTOR`     | `Qwen3.6-Mesh-Structured`      | Translate intent into a concrete pi prompt               |
| `CODER`        | `Qwen3.6-Mesh-Code-Long`       | The pi backing model (writes/edits files; thinking off by default in CLI) |
| `WRITER`       | `Qwen3.6-Mesh-Thinking-Long`   | Long prose — currently unused; doc tasks use CODER       |
| `JUDGE_VISION` | `Qwen3.6-Mesh`                 | First-pass describe (vision)                             |
| `JUDGE_TEXT`   | `Qwen3.6-Mesh-Structured`      | First-pass describe (text-only) + verdict pass           |

Override any of these with environment variables, e.g.
`THELOOP_MODEL_JUDGE_VISION=Qwen3.6-Mesh-Thinking`.

## What's next

- Filter `__pycache__` and similar from the `doc` adapter's `context/` copy
- Render at higher resolution (1024 → 1536) to give the vision encoder more
  detail to verify structural integrity
- Adversarial describe is generic across adapters but the prompt could be
  specialized per artifact type for sharper element extraction
- Resumable runs (currently a re-run starts from scratch)

## Layout

```
src/theloop/
  cli.py            # Typer entry point; wires Workspace, Adapter, Loop
  loop.py           # Per-iter sequence: plan → direct → pi → check → render → judge → commit
  orchestrator.py   # Two agno Agents: planner (intent + spec) and director (prompt for pi)
  pi_client.py      # JSON-RPC stdio wrapper around `pi --mode rpc`
  renderer.py       # async Playwright wrapper, headless Chromium screenshots
  judge.py          # Two-pass judge: adversarial describe + verdict
  terminator.py     # done | threshold | plateau | max_iters
  workspace.py      # Per-run git working tree, branch-per-iter
  reporter.py       # JSONL events + self-contained HTML report
  models.py         # Hat enum + alias resolution
  adapters/
    base.py         # TaskAdapter ABC
    svg.py          # SVG → Chromium screenshot
    web.py          # HTML/JS/CSS → Chromium screenshot
    doc.py          # Markdown improvement, with context/ reference material
    generic.py      # No render — text judge against spec + assistant turn
  prompts/
    planner.md, director.md, judge.md, judge_describe.md

examples/           # specs covering all four adapters
docs/               # design notes
runs/               # generated per-run output (gitignored)
```

## License

TBD.
