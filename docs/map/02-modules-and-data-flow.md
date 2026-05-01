# theloop — Repository Map (Sections 3–4)

## 3. 🧩 MODULE / COMPONENT MAPPING

### 3.1 `theloop.cli` — CLI Wiring

- **Purpose**: Typer CLI that parses spec files, resolves configuration, wires all components, and launches the async loop. The **only** place that knows how to construct and connect every piece.
- **Public API**:
  - `app = typer.Typer()` — Typer app instance
  - `run(spec_path, ...)` → `@app.command()` — main loop execution
  - `report(run_dir)` → `@app.command()` — HTML report regeneration
- **Internal Deps**:
  - `from theloop.adapters import get_adapter` [CONFIRMED]
  - `from theloop.judge import Judge` [CONFIRMED]
  - `from theloop.loop import Loop` [CONFIRMED]
  - `from theloop.models import Hat, alias_for` [CONFIRMED]
  - `from theloop.orchestrator import Orchestrator` [CONFIRMED]
  - `from theloop.pi_client import PiClient` [CONFIRMED]
  - `from theloop.renderer import Renderer` [CONFIRMED]
  - `from theloop.reporter import Reporter, build_html_report` [CONFIRMED]
  - `from theloop.terminator import TerminationConfig, Terminator` [CONFIRMED]
  - `from theloop.workspace import Workspace, make_run_id` [CONFIRMED]
- **Key Files**:
  - `cli.py` → Parses YAML frontmatter, builds `TerminationConfig`, creates all components, calls `Loop.run()`, prints summary. Contains `_ADAPTER_NOTES` dict with per-adapter pi guidance strings.
- **Data Flow**: Reads spec.md → parses frontmatter → configures adapter → wires components → runs loop → prints summary → builds HTML report.
- **Testing**: No dedicated CLI tests. Smoke tested via `python -m theloop run examples/pelican.spec.md`.
- **Confidence**: 100% [CONFIRMED]

### 3.2 `theloop.loop` — Main Control Flow

- **Purpose**: The `Loop` class owns the per-iteration control flow. It is the central orchestrator that sequences: plan → direct → pi → runtime_check → render → judge → commit → terminator. It owns no LLM state; all persistence is delegated to `Workspace` and `Reporter`.
- **Public API**:
  - `class Loop` → `async def run() → RunResult`
  - `@dataclass IterationRecord` → per-iteration snapshot
  - `@dataclass RunResult` → final run summary
- **Internal Deps**:
  - `from theloop.adapters.base import RuntimeCheckResult, TaskAdapter` [CONFIRMED]
  - `from theloop.judge import Judge, JudgeVerdict` [CONFIRMED]
  - `from theloop.orchestrator import Orchestrator, PlanResult` [CONFIRMED]
  - `from theloop.pi_client import PiClient, PiResult` [CONFIRMED]
  - `from theloop.renderer import Renderer` [CONFIRMED]
  - `from theloop.reporter import Reporter` [CONFIRMED]
  - `from theloop.terminator import StopReason, Terminator` [CONFIRMED]
  - `from theloop.workspace import Workspace` [CONFIRMED]
- **Key Files**:
  - `loop.py` → `_run_one()` executes the per-iteration pipeline. `_run_pi_with_retry()` handles timeout + retry logic. `_prewrite_policy_violation()` enforces bounded tool use before first write. `_compose_pi_retry_prompt()` generates corrective prompts. `_write_pi_live_event()` writes compact live traces.
- **Data Flow**: Receives spec + all components → iterates → emits events to Reporter → returns RunResult with full iteration history.
- **Testing**: `test_loop_retry_prompt.py` covers `_compose_pi_retry_prompt()` and `_prewrite_policy_violation()`.
- **Confidence**: 100% [CONFIRMED]

### 3.3 `theloop.orchestrator` — Planner + Director Hats

- **Purpose**: Wraps two agno `Agent` instances (planner + director), each backed by a different LiteLLM model alias. The planner evolves the spec and produces iteration intents; the director translates intents into concrete prompts for pi.
- **Public API**:
  - `class Orchestrator` → `async def plan(spec, critique, description) → PlanResult`
  - `async def direct(spec, intent, workspace, adapter_notes) → str`
- **Internal Deps**:
  - `from agno.agent import Agent` [CONFIRMED]
  - `from agno.models.openai import OpenAIChat` [CONFIRMED]
  - `from pydantic import BaseModel, Field` [CONFIRMED]
  - `from theloop.models import Hat, LiteLLMConfig, alias_for, litellm_config` [CONFIRMED]
  - `from theloop.adapters.svg import SVGAdapter` [NEEDS_VERIFICATION — only in _smoke()]
- **Key Files**:
  - `orchestrator.py` → `_parse_plan()` parses JSON output with fallback. `_preserves_spec()` prevents spec rewriting. `_retarget_spec_edit_intent()` converts spec-change intents into artifact work. `_compose_pi_prompt()` assembles the final pi prompt. `_workspace_inventory()` lists workspace files.
- **Data Flow**: Receives spec + critique → planner produces updated spec + intent → director produces pi prompt.
- **Testing**: `test_orchestrator_plan.py` covers spec preservation, intent coercion, anti-pattern rejection.
- **Confidence**: 95% [CONFIRMED, minor inference on _smoke() import]

### 3.4 `theloop.pi_client` — Pi Subprocess Wrapper

- **Purpose**: Async context manager that spawns `pi --mode rpc` as a subprocess, communicates via line-delimited JSON over stdin/stdout, and collects events into a `PiResult`. Handles session lifecycle, prompt sending, and stderr capture.
- **Public API**:
  - `class PiClient` → `async def __aenter__()`, `async def new_session()`, `async def prompt(text, on_event, timeout) → PiResult`
  - `@dataclass PiResult` → assistant_text, tool_calls, touched_files, event_count, messages
  - `class PiError` → subprocess failure exception
- **Internal Deps**:
  - `asyncio`, `json`, `os`, `collections.deque`, `dataclasses`, `pathlib`, `typing` [stdlib]
  - No external library deps (pure subprocess + JSON)
- **Key Files**:
  - `pi_client.py` → `_absorb()` extracts tool calls and assistant text from events. `_path_is_outside_workspace()` detects absolute-path hallucinations. `_stderr_tail()` captures stderr for crash diagnosis.
- **Data Flow**: Spawns pi subprocess → sends prompt → streams events → collects tool calls + touched files + assistant text → returns PiResult.
- **Testing**: No dedicated unit tests. Manual smoke test in `_smoke()`.
- **Confidence**: 100% [CONFIRMED]

### 3.5 `theloop.renderer` — Headless Screenshot

- **Purpose**: Async Playwright wrapper that launches Chromium once per run and takes screenshots of workspace HTML pages. Each screenshot uses a fresh `BrowserContext` to avoid state leakage between iterations.
- **Public API**:
  - `class Renderer` → `async def __aenter__()`, `async def __aexit__()`, `async def screenshot(url, out_png, ...)`
  - `class RendererError` → runtime exception
  - `DEFAULT_VIEWPORT = (1536, 1152)` — increased from prior 1024×768
- **Internal Deps**:
  - `from playwright.async_api import Browser, Playwright, async_playwright` [CONFIRMED]
- **Key Files**:
  - `renderer.py` → `screenshot()` sets up console error capture, navigates to file:// URL, waits for `wait_for_js` expression, captures PNG.
- **Data Flow**: Receives file:// URL + output path → launches browser context → navigates → screenshots → writes PNG.
- **Testing**: Manual smoke test in `_smoke()`. No pytest tests.
- **Confidence**: 100% [CONFIRMED]

### 3.6 `theloop.judge` — Two-Pass Evaluation

- **Purpose**: Evaluates artifacts against specs using a two-pass design: (1) describe pass classifies elements as PRESENT/PARTIAL/HIDDEN/MISSING, (2) verdict pass scores from those classifications using a weighted formula. Includes deterministic guards against known failure modes (position contradictions, spatial layout failures).
- **Public API**:
  - `class Judge` → `async def vision_probe() → bool`, `async def evaluate(spec, png_path, last_pi_output, artifact_text) → JudgeVerdict`
  - `@dataclass JudgeVerdict` → score, critique, done, raw, description
- **Internal Deps**:
  - `from openai import AsyncOpenAI` [CONFIRMED]
  - `from theloop.models import Hat, LiteLLMConfig, alias_for, litellm_config` [CONFIRMED]
- **Key Files**:
  - `judge.py` → `_describe()` handles vision vs text paths. `_parse_verdict()` parses JSON with fallback. `_apply_description_score_guard()` enforces score bounds from classifications. `_apply_position_contradiction_guard()` downgrades hands at wrong clock positions. `_apply_spatial_layout_guard()` penalizes gears outside watch case. `_score_from_description()` computes weighted score from classifications.
- **Data Flow**: Receives spec + render PNG + pi output → describe pass → verdict pass → JudgeVerdict.
- **Testing**: `test_judge_scoring.py` covers scoring formula, description guards, position contradictions, spatial layout guards.
- **Confidence**: 100% [CONFIRMED]

### 3.7 `theloop.terminator` — Stop Conditions

- **Purpose**: Pure function that evaluates composite stop conditions over judge verdict history. No I/O, no LLM calls.
- **Public API**:
  - `class Terminator` → `def should_stop(history) → StopReason | None`
  - `@dataclass TerminationConfig` → max_iters, score_threshold, no_improvement_for
  - `class StopReason(StrEnum)` → DONE, THRESHOLD, PLATEAU, MAX_ITERS
- **Internal Deps**:
  - `from theloop.judge import JudgeVerdict` [CONFIRMED — circular import avoided via TYPE_CHECKING or late import]
- **Key Files**:
  - `terminator.py` → `_best()` extracts max score from a list of verdicts. Priority: done > threshold > plateau > max_iters.
- **Data Flow**: Receives list of JudgeVerdicts → evaluates conditions in priority order → returns first matching StopReason or None.
- **Testing**: Self-test in `_smoke()` covers all stop-condition combinations.
- **Confidence**: 100% [CONFIRMED]

### 3.8 `theloop.workspace` — Git Per-Iteration

- **Purpose**: Manages per-run isolated git working trees. Each run gets its own `runs/<id>/workspace/` repo with one branch per iteration (`iter/0`, `iter/1`, ...). Handles reconciliation of pi writes that land outside the workspace.
- **Public API**:
  - `class Workspace` → `@classmethod create()`, `@classmethod open()`, `begin_iteration()`, `commit_iteration()`, `diff_iteration()`, `reconcile_external_writes()`
  - `def make_run_id(slug, now) → str` → `YYYYMMDD-HHMMSS[-slug]`
- **Internal Deps**:
  - `import git` (GitPython) [CONFIRMED]
  - `pathlib`, `datetime`, `shutil`, `logging`, `re` [stdlib]
- **Key Files**:
  - `workspace.py` → `reconcile_external_writes()` maps pi writes from run root back into workspace. `commit_iteration()` creates branch, stages all files, commits with intent-based message.
- **Data Flow**: Creates git repo → iter 0 checks out main → pi edits → iter N checks out parent branch → pi edits → commit_iteration creates `iter/N` branch.
- **Testing**: `test_workspace_reconcile.py` covers external write reconciliation.
- **Confidence**: 100% [CONFIRMED]

### 3.9 `theloop.reporter` — Event Logging + HTML Report

- **Purpose**: Append-only JSONL event log (`events.jsonl`) and static HTML report builder. Every component calls `reporter.emit()` at lifecycle boundaries.
- **Public API**:
  - `class Reporter` → `def emit(kind, iter, **payload)`, `def close()`, context manager
  - `def build_html_report(run_dir) → Path` → generates `index.html` + per-iter `diff.txt`
- **Internal Deps**:
  - `json`, `html`, `logging`, `collections.defaultdict`, `datetime`, `pathlib`, `typing` [stdlib]
  - `import git` (conditional, inside `build_html_report`) [CONFIRMED]
- **Key Files**:
  - `reporter.py` → `_render_html()` builds self-contained HTML with cards per iteration. `_render_iter_card()` assembles per-iteration card with render image, intent, critique, runtime check, commit info.
- **Data Flow**: Events emitted during loop → JSONL written → `build_html_report()` reads JSONL + git diffs → writes `index.html`.
- **Testing**: Manual smoke test in `_smoke()`. No pytest tests.
- **Confidence**: 100% [CONFIRMED]

### 3.10 `theloop.models` — Hat → Alias Mapping

- **Purpose**: Defines the `Hat` enum (PLANNER, DIRECTOR, CODER, WRITER, JUDGE_VISION, JUDGE_TEXT) and maps each to a LiteLLM alias. Supports env-var override via `THELOOP_MODEL_<HAT>`. Loads LiteLLM config from environment.
- **Public API**:
  - `class Hat(StrEnum)` → 6 hats
  - `def alias_for(hat) → str` → env override or default
  - `@dataclass LiteLLMConfig` → base_url, api_key
  - `def litellm_config() → LiteLLMConfig` → reads from env
- **Internal Deps**:
  - `os`, `dataclasses`, `enum` [stdlib]
- **Key Files**:
  - `models.py` → `_DEFAULT_ALIAS` dict maps hats to aliases. `litellm_config()` raises KeyError if env vars missing.
- **Data Flow**: Env vars → `litellm_config()` → config passed to Orchestrator, Judge, PiClient.
- **Testing**: Manual smoke test in `_smoke()`. No pytest tests.
- **Confidence**: 100% [CONFIRMED]

### 3.11 `theloop.adapters` — Task Adapter Registry

- **Purpose**: Plugin system for task-type-specific behavior. Each adapter defines how to scaffold the workspace, validate the artifact, render it to PNG, and extract text for the judge.
- **Public API**:
  - `get_adapter(name) → TaskAdapter` — registry lookup
  - `ADAPTERS: dict[str, type[TaskAdapter]]` — registry dict
  - `class TaskAdapter(ABC)` — base class
  - `class RuntimeCheckResult` — ok + log
- **Internal Deps**:
  - `adapters/svg.py` → `from theloop.renderer import Renderer` [CONFIRMED]
  - `adapters/web.py` → `from theloop.renderer import Renderer` [CONFIRMED]
  - `adapters/doc.py` → `from theloop.renderer import Renderer` [CONFIRMED]
  - `adapters/generic.py` → `from theloop.renderer import Renderer` [CONFIRMED]
  - `adapters/base.py` → `from theloop.renderer import Renderer` (late import to avoid circular) [CONFIRMED]
- **Key Files**:
  - `base.py` → `TaskAdapter` ABC with `prepare()`, `runtime_check()`, `render()`, `artifact_text()`, `configure()`, `extra_director_notes()`.
  - `svg.py` → XML parse check, inline SVG in HTML, Chromium screenshot.
  - `web.py` → HTML parse check, `__ready` signal, three.js CDN scaffold.
  - `doc.py` → Source document copy, context/ reference material, text-only judge.
  - `generic.py` → Minimal scaffold, permissive runtime check, no render.
- **Data Flow**: CLI selects adapter → adapter.prepare() scaffolds workspace → adapter.runtime_check() validates after pi → adapter.render() produces PNG → adapter.artifact_text() extracts text for judge.
- **Testing**: Each adapter has a `_smoke()` manual test. No pytest tests for adapters.
- **Confidence**: 100% [CONFIRMED]

### 3.12 `theloop.prompts` — Prompt Templates

- **Purpose**: Markdown prompt templates that define the behavior of each LLM role. Loaded at construction time by their respective components.
- **Files**:
  - `planner.md` → Planner role: spec evolution, iteration intent, anti-patterns
  - `director.md` → Director role: intent → pi prompt, workspace inventory, adapter notes
  - `judge.md` → Judge verdict pass: weighted scoring formula, subject-missing floor
  - `judge_describe.md` → Judge describe pass: PRESENT/PARTIAL/HIDDEN/MISSING classification
- **Confidence**: 100% [CONFIRMED]

---

## 4. 💧 DATA & STATE FLOW

### 4.1 Core Data Models

| Model | File | Fields | Used By |
|-------|------|--------|---------|
| `Hat` (StrEnum) | `models.py` | PLANNER, DIRECTOR, CODER, WRITER, JUDGE_VISION, JUDGE_TEXT | All LLM-calling components |
| `LiteLLMConfig` (dataclass) | `models.py` | base_url: str, api_key: str | Orchestrator, Judge, PiClient |
| `PlanResult` (dataclass) | `orchestrator.py` | spec: str, intent: str | Loop → Orchestrator → Loop |
| `RuntimeCheckResult` (dataclass) | `adapters/base.py` | ok: bool, log: str | Loop → Adapter → Loop |
| `PiResult` (dataclass) | `pi_client.py` | assistant_text, tool_calls, touched_files, event_count, messages | Loop → PiClient → Loop |
| `JudgeVerdict` (dataclass) | `judge.py` | score: float\|None, critique: str, done: bool, raw: str, description: str | Loop → Judge → Terminator |
| `TerminationConfig` (dataclass) | `terminator.py` | max_iters: int, score_threshold: float, no_improvement_for: int | CLI → Terminator |
| `StopReason` (StrEnum) | `terminator.py` | DONE, THRESHOLD, PLATEAU, MAX_ITERS | Terminator → Loop |
| `IterationRecord` (dataclass) | `loop.py` | iter, intent, spec, pi_assistant_text, pi_touched, runtime_check, render_png, verdict, commit_sha | Loop → RunResult |
| `RunResult` (dataclass) | `loop.py` | run_id, run_dir, stop_reason, best_score, iterations | Loop → CLI |

### 4.2 Storage & State

| Storage | Location | Purpose |
|---------|----------|---------|
| **Git repo** | `runs/<id>/workspace/` | Per-run isolated workspace, one branch per iteration |
| **JSONL events** | `runs/<id>/events.jsonl` | Append-only event log for all loop boundaries |
| **HTML report** | `runs/<id>/index.html` | Self-contained static report |
| **Per-iter artifacts** | `runs/<id>/artifacts/iter-N/` | render.png, judge_description.txt, pi_prompt.txt, pi_assistant.txt, spec.md, diff.txt, pi_live.log |
| **Workspace files** | `runs/<id>/workspace/` | Pi-edited artifacts (artifact.svg, index.html, document.md, etc.) |
| **Environment** | `.env` (project root) | LITELLM_BASE_URL, LITELLM_MASTER_KEY, PI_CODING_AGENT_DIR, THELOOP_MODEL_* |

### 4.3 Data Transformation Pipelines

```
Spec (markdown + YAML frontmatter)
  │
  ├─ _parse_frontmatter() → (fm: dict, body: str)
  ├─ _normalize_spec_text() → compacted markdown (no extra blank lines, code fences preserved)
  │
  ▼
Planner: spec + critique + description
  │
  ├─ _normalize_markdown() → compacted
  ├─ json.loads() → {spec, intent}
  ├─ _preserves_spec() → reject if spec rewritten
  ├─ _retarget_spec_edit_intent() → convert spec-change → artifact work
  │
  ▼
Updated spec + intent
  │
  ▼
Director: spec + intent + workspace inventory + adapter notes
  │
  ├─ _workspace_inventory() → file listing
  ├─ _normalize_markdown() → compacted
  ├─ _compose_pi_prompt() → final prompt
  │
  ▼
Pi prompt → Pi subprocess → PiResult (assistant_text, tool_calls, touched_files)
  │
  ▼
Adapter: runtime_check() → RuntimeCheckResult(ok, log)
  │
  ├─ SVG: ET.parse() → XML validation
  ├─ Web: HTMLParser → tag balance check
  ├─ Doc: file exists + non-empty
  ├─ Generic: file count > 0
  │
  ▼
Adapter: render() → PNG (if visual)
  │
  ▼
Judge: describe pass → classification (PRESENT/PARTIAL/HIDDEN/MISSING)
  │
  ├─ Vision: base64 image + spec → description
  ├─ Text: artifact text (trimmed to 12KB) + spec → description
  │
  ▼
Judge: verdict pass → JSON {score, critique, done}
  │
  ├─ _parse_verdict() → JSON parse
  ├─ _apply_description_score_guard() → enforce score bounds
  ├─ _apply_position_contradiction_guard() → downgrade hands at wrong positions
  ├─ _apply_spatial_layout_guard() → penalize gears outside case
  │
  ▼
JudgeVerdict → Terminator → StopReason | None
```

### 4.4 Event Schema (Reporter)

Each event in `events.jsonl`:
```json
{
  "ts": "2026-05-01T08:49:00.123456+00:00",
  "iter": 0,
  "kind": "plan_start",
  "payload": { ... }
}
```

Event kinds emitted (from code analysis):
- `run_start`, `run_end`
- `scaffold`
- `plan_start`, `plan_end`
- `direct_start`, `direct_end`
- `pi_start`, `pi_end`, `pi_progress`, `pi_timeout`, `pi_retry_start`, `pi_retry_failed`, `pi_live_log`, `pi_tool_start`, `pi_tool_end`, `pi_prewrite_policy_timeout`, `pi_no_write_timeout`, `pi_reconciled_writes`, `pi_no_workspace_changes`
- `runtime_check`
- `render`, `render_error`
- `judge_start`, `judge_end`
- `commit`, `commit_error`
- `iter_end`

[CONFIRMED]

---

*Continued in: `03-dependencies-config-testing-gaps.md`*
