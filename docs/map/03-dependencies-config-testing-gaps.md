# theloop — Repository Map (Sections 5–8)

## 5. 🔗 DEPENDENCIES & INTEGRATIONS

### 5.1 External Dependencies

| Package | Version | Purpose | Used In |
|---------|---------|---------|---------|
| `agno` | 2.6.4 | Agent orchestration (LLM calls) | `orchestrator.py` |
| `openai` | 2.33.0 | OpenAI-compatible HTTP client (LiteLLM proxy) | `judge.py`, `models.py` (via agno) |
| `playwright` | 1.58.0 | Headless Chromium for screenshots | `renderer.py`, `adapters/svg.py`, `adapters/web.py` |
| `pydantic` | 2.13.3 | Data validation (PlanOutput model) | `orchestrator.py` |
| `python-dotenv` | 1.2.2 | .env file loading | `__init__.py` |
| `typer` | 0.25.0 | CLI framework | `cli.py` |
| `GitPython` | 3.1.48 | Git operations | `workspace.py`, `reporter.py` |
| `PyYAML` | 6.0.3 | YAML frontmatter parsing | `cli.py` |

**Transitive deps** (from `requirements.txt`): `httpx`, `anyio`, `sniffio`, `idna`, `certifi`, `h11`, `h2`, `hpack`, `hyperframe`, `pydantic_core`, `pydantic-settings`, `typing-inspection`, `typing_extensions`, `rich`, `shellingham`, `click`, `gitdb`, `smmap`, `greenlet`, `pyee`, `markdown-it-py`, `mdurl`, `Pygments`, `docstring_parser`, `packaging`, `python-multipart`, `annotated-doc`, `annotated-types`.

### 5.2 External Services

| Service | Address | Purpose | Config |
|---------|---------|---------|--------|
| **LiteLLM proxy** | `$LITELLM_BASE_URL` (default: `http://100.80.49.81:4000`) | Model routing, alias resolution, sampling presets | `.env` → `LITELLM_BASE_URL`, `LITELLM_MASTER_KEY` |
| **Pi coding agent** | `pi --mode rpc` (global npm binary) | Code generation via read/write/edit/bash tools | `.env` → `PI_CODING_AGENT_DIR=~/.pi` |

### 5.3 Internal Cross-Module References

```
cli.py
  ├── adapters/__init__.py → get_adapter()
  ├── judge.py → Judge
  ├── loop.py → Loop
  ├── models.py → Hat, alias_for
  ├── orchestrator.py → Orchestrator
  ├── pi_client.py → PiClient
  ├── renderer.py → Renderer
  ├── reporter.py → Reporter, build_html_report
  ├── terminator.py → TerminationConfig, Terminator
  └── workspace.py → Workspace, make_run_id

loop.py
  ├── adapters/base.py → RuntimeCheckResult, TaskAdapter
  ├── judge.py → Judge, JudgeVerdict
  ├── orchestrator.py → Orchestrator, PlanResult
  ├── pi_client.py → PiClient, PiResult
  ├── renderer.py → Renderer
  ├── reporter.py → Reporter
  ├── terminator.py → StopReason, Terminator
  └── workspace.py → Workspace

orchestrator.py
  ├── agno.agent → Agent
  ├── agno.models.openai → OpenAIChat
  ├── pydantic → BaseModel, Field
  └── models.py → Hat, LiteLLMConfig, alias_for, litellm_config

pi_client.py
  └── (no internal deps — pure subprocess + JSON)

renderer.py
  └── playwright.async_api → Browser, Playwright, async_playwright

judge.py
  ├── openai → AsyncOpenAI
  └── models.py → Hat, LiteLLMConfig, alias_for, litellm_config

terminator.py
  └── judge.py → JudgeVerdict (late import to avoid circular)

workspace.py
  └── git → git.Repo

reporter.py
  └── git (conditional import inside build_html_report)

models.py
  └── (no internal deps — pure env + dataclass)

adapters/base.py
  └── renderer.py (late import for type annotation only)

adapters/svg.py
  ├── adapters/base.py → RuntimeCheckResult, TaskAdapter
  └── renderer.py → Renderer

adapters/web.py
  ├── adapters/base.py → RuntimeCheckResult, TaskAdapter
  └── renderer.py → Renderer

adapters/doc.py
  ├── adapters/base.py → RuntimeCheckResult, TaskAdapter
  └── renderer.py → Renderer

adapters/generic.py
  ├── adapters/base.py → RuntimeCheckResult, TaskAdapter
  └── renderer.py → Renderer
```

### 5.4 Circular Dependency Analysis

| Potential Cycle | Resolution |
|-----------------|------------|
| `terminator.py` → `judge.py` → `terminator.py` | `terminator.py` imports `JudgeVerdict` from `judge.py` at module level. `judge.py` does NOT import `terminator.py`. **No cycle.** [CONFIRMED] |
| `adapters/base.py` → `renderer.py` → `adapters/base.py` | `base.py` imports `Renderer` at the bottom of the file (after class definition) to avoid circular import. `renderer.py` does NOT import `adapters/base.py`. **No cycle.** [CONFIRMED] |
| `__init__.py` → `cli.py` → `loop.py` → `orchestrator.py` → `models.py` → `__init__.py` | `__init__.py` only loads `.env`. No circular import chain. [CONFIRMED] |

[CONFIRMED]

---

## 6. ⚙️ CONFIGURATION & ENVIRONMENT

### 6.1 Environment Variables

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `LITELLM_BASE_URL` | Yes | — | LiteLLM proxy endpoint (e.g., `http://100.80.49.81:4000`) |
| `LITELLM_MASTER_KEY` | Yes | — | Master API key for LiteLLM proxy |
| `PI_CODING_AGENT_DIR` | No | `~/.pi` | Pi agent configuration directory |
| `THELOOP_MODEL_PLANNER` | No | `Qwen3.6-Mesh-Thinking-Long` | Override planner model alias |
| `THELOOP_MODEL_DIRECTOR` | No | `Qwen3.6-Mesh-Structured` | Override director model alias |
| `THELOOP_MODEL_CODER` | No | `Qwen3.6-Mesh-Code-Long` | Override pi backing model alias |
| `THELOOP_MODEL_WRITER` | No | `Qwen3.6-Mesh-Thinking-Long` | Override writer model alias |
| `THELOOP_MODEL_JUDGE_VISION` | No | `Qwen3.6-Mesh` | Override judge vision model alias |
| `THELOOP_MODEL_JUDGE_TEXT` | No | `Qwen3.6-Mesh-Structured` | Override judge text model alias |

### 6.2 Spec Frontmatter Configuration

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `adapter` | string | (required) | Task adapter: `svg`, `web`, `doc`, `generic` |
| `max_iters` | int | 10 | Maximum iterations |
| `score_threshold` | float | 0.85 | Score at which to stop |
| `no_improvement_for` | int | 3 | Plateau detection window |
| `source` | string | (required for `doc`) | Path to source document |
| `rubric` | string | (optional for `doc`) | Path to rubric file |
| `context` | list | [] | Read-only reference material paths |
| `context_notes` | string | "" | Task-specific notes for director |

### 6.3 CLI Overrides

| Flag | Overrides | Default |
|------|-----------|---------|
| `--adapter` | frontmatter `adapter` | (required) |
| `--max-iters` | frontmatter `max_iters` | 10 |
| `--threshold` | frontmatter `score_threshold` | 0.85 |
| `--no-improvement-for` | frontmatter `no_improvement_for` | 3 |
| `--run-id` | auto-generated ID | `YYYYMMDD-HHMMSS[-slug]` |
| `--pi-timeout-s` | per-iteration pi timeout | 600.0 |
| `--pi-no-write-timeout-s` | no-write timeout | 120.0 |
| `--pi-thinking` | pi thinking level | `off` |
| `--pi-no-session` | ephemeral pi sessions | `False` |
| `--log-level` | Python logging level | `INFO` |

### 6.4 Secrets Strategy

- **Strategy**: `.env` file at project root, loaded by `python-dotenv` on first `import theloop`.
- **Risk**: `.env` is NOT gitignored (`.gitignore` does not list `.env`). Contains plaintext API keys.
- **Mitigation**: None detected. No secret rotation, no vault integration.

### 6.5 Multi-Environment Setup

- **Not implemented.** Single `.env` file for all environments. No dev/stage/prod separation.
- The LiteLLM proxy address is hardcoded in `.env` (`http://100.80.49.81:4000`).
- The `litellm-endpoints.md` doc describes two alternative config blocks (35B vs 27B backbones) that are swapped on the proxy side — code is proxy-agnostic.

[CONFIRMED]

---

## 7. 🧪 TESTING, QUALITY & CONVENTIONS

### 7.1 Test Structure

| Test File | Coverage | Strategy |
|-----------|----------|----------|
| `test_judge_scoring.py` | Judge scoring formula, description guards, position contradictions, spatial layout guards | Direct function calls, no mocking |
| `test_loop_retry_prompt.py` | Retry prompt constraints, pre-write policy violations | Direct function calls, no mocking |
| `test_orchestrator_plan.py` | Spec preservation, intent coercion, anti-pattern rejection | Direct function calls, no mocking |
| `test_workspace_reconcile.py` | External write reconciliation | `tmp_path` fixture, real filesystem |

### 7.2 Test Gaps

| Module | Has Tests? | Notes |
|--------|-----------|-------|
| `cli.py` | ❌ | No dedicated tests. Integration tested via `python -m theloop run` |
| `loop.py` | Partial | Only `_compose_pi_retry_prompt` and `_prewrite_policy_violation` tested (these are module-level functions, not Loop class methods) |
| `orchestrator.py` | Partial | Only `_parse_plan`, `_compose_pi_prompt`, `_normalize_markdown` tested. `plan()` and `direct()` require live LLM proxy |
| `pi_client.py` | ❌ | No tests. Requires live `pi` binary |
| `renderer.py` | ❌ | No tests. Requires Playwright + Chromium |
| `judge.py` | Partial | Only `_parse_verdict`, `_score_from_description` tested. `evaluate()` and `vision_probe()` require live LLM proxy |
| `terminator.py` | ✅ | Self-test in `_smoke()` covers all conditions. No pytest tests |
| `workspace.py` | Partial | Only `reconcile_external_writes` tested. `begin_iteration`, `commit_iteration`, `diff_iteration` not tested |
| `reporter.py` | ❌ | No tests. Requires filesystem + git |
| `models.py` | ❌ | No tests |
| `adapters/` | ❌ | No pytest tests. Each has `_smoke()` manual test |

### 7.3 Quality & Conventions

| Aspect | Convention | Evidence |
|--------|-----------|----------|
| **Naming** | snake_case for functions/variables, PascalCase for classes, UPPER_SNAKE for constants | Consistent across all files |
| **Type hints** | Full type annotations, `from __future__ import annotations` | All source files |
| **Dataclasses** | `@dataclass(frozen=True, slots=True)` for immutable records | `PlanResult`, `RuntimeCheckResult`, `PiResult`, `JudgeVerdict`, `TerminationConfig`, `IterationRecord`, `RunResult`, `LiteLLMConfig` |
| **Error handling** | Fail-fast on missing env vars (`litellm_config()` raises `KeyError`), graceful fallbacks on LLM parse failures | `models.py`, `judge.py`, `orchestrator.py` |
| **Logging** | `logging.getLogger(__name__)` pattern, INFO default, httpx/openai silenced at INFO | All modules |
| **Architecture** | Dependency injection via constructor args. CLI is the only wiring layer. Loop owns no LLM state. | `Loop.__init__`, `Orchestrator.__init__`, `Judge.__init__` |
| **Prompt engineering** | Markdown templates with explicit anti-patterns, hard rules, and output shape constraints | All prompt files |
| **Code style** | No linter/formatter config detected. Consistent 4-space indentation. | No `ruff.toml`, `.pre-commit-config.yaml`, etc. |

### 7.4 Architecture Style

**Hexagonal / Ports-and-Adapters** with a **pipeline** control flow:
- The `Loop` class is the central pipeline, sequencing discrete stages.
- `TaskAdapter` is the adapter port — swappable implementations for different artifact types.
- `Reporter` is the event-sourcing port — all state changes emit events.
- `Workspace` is the persistence port — git-backed per-run isolation.
- `Terminator` is a pure function — no side effects, fully testable.

**Not MVC** (no views/controllers in the traditional sense). **Not event-driven** (synchronous pipeline, not pub/sub). **Not CQRS** (no command/query separation).

[CONFIRMED]

---

## 8. 🔍 GAP ANALYSIS & VERIFICATION

### 8.1 Undocumented Logic

| Location | Issue | Confidence |
|----------|-------|------------|
| `loop.py: _prewrite_policy_violation()` | The pre-write tool budget logic (8 tools for first attempt, 4 for retry) is undocumented outside the code. The rationale is in `regression-recovery-2026-05-01.md` but not in `spec.md`. | [CONFIRMED] |
| `loop.py: _section()` | Helper function extracts text between two markers in the prompt. Used by `_compose_pi_retry_prompt()` to extract directive and spec. Not documented. | [CONFIRMED] |
| `loop.py: _write_pi_live_event()` | Complex event-to-log formatting with state tracking for text/thinking chunks. ~80 lines of formatting logic. Not documented. | [CONFIRMED] |
| `judge.py: _apply_position_contradiction_guard()` | Hardcoded logic for "hour hand at 12 when spec says 10" and "minute hand at 12 when spec says 2". Domain-specific to clock/watch specs. | [CONFIRMED] |
| `judge.py: _apply_spatial_layout_guard()` | Hardcoded logic for "gears outside watch case". Domain-specific to mechanical watch specs. | [CONFIRMED] |
| `orchestrator.py: _preserves_spec()` | Heuristic spec preservation: length ratio (0.8×–2.5×), SVG presence check, frontmatter equality, contract comparison. Not documented in spec.md. | [CONFIRMED] |
| `workspace.py: reconcile_external_writes()` | Complex path reconciliation logic for pi writes that land outside workspace. Rationale in regression notes. | [CONFIRMED] |

### 8.2 Ambiguous Imports

| Location | Issue | Verification |
|----------|-------|-------------|
| `terminator.py` → `from theloop.judge import JudgeVerdict` | Imports a dataclass from another module. If `judge.py` were refactored to move `JudgeVerdict`, this would break. | [CONFIRMED] |
| `adapters/base.py` → `from theloop.renderer import Renderer` | Late import at bottom of file to avoid circular dependency. The import is only used for a type annotation in the abstract method signature. | [CONFIRMED] |
| `reporter.py` → `import git` (conditional) | Git is imported inside `build_html_report()`, not at module level. This means the function fails at runtime if GitPython is not installed, even though it's a declared dependency. | [CONFIRMED] |

### 8.3 Missing Tests

| Module | Missing Test Coverage | Priority |
|--------|----------------------|----------|
| `cli.py` | Full CLI integration test (spec parsing, frontmatter, adapter resolution) | High |
| `loop.py` | `Loop.run()` integration test (mocked components) | High |
| `loop.py` | `_run_pi_with_retry()` timeout + retry logic | High |
| `loop.py` | `pi_no_workspace_changes` path (no-op iteration) | Medium |
| `orchestrator.py` | `plan()` with live LLM (requires proxy) | Low (integration) |
| `orchestrator.py` | `direct()` with live LLM (requires proxy) | Low (integration) |
| `pi_client.py` | All subprocess lifecycle tests | High |
| `renderer.py` | Screenshot with Playwright | Medium |
| `judge.py` | `evaluate()` end-to-end (requires proxy) | Low (integration) |
| `judge.py` | `vision_probe()` success/failure paths | Medium |
| `terminator.py` | pytest tests (currently only `_smoke()`) | Low |
| `workspace.py` | `begin_iteration()`, `commit_iteration()`, `diff_iteration()` | Medium |
| `reporter.py` | `build_html_report()` output validation | Medium |
| `models.py` | `alias_for()` env override behavior | Low |
| `adapters/` | All adapter implementations | Medium |

### 8.4 Potential Dead Code

| Location | Issue | Confidence |
|----------|-------|------------|
| `models.py: Hat.WRITER` | Defined but never used. Doc tasks use `Hat.CODER` instead. Comment in `cli.py` says "doc tasks use CODER". | [CONFIRMED] |
| `models.py: main()` | `if __name__ == "__main__"` block prints config. Not used in production. | [CONFIRMED] |
| `orchestrator.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `judge.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `pi_client.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `renderer.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `workspace.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `reporter.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `terminator.py: _smoke()` | Self-test. Not a pytest test. | [CONFIRMED] |
| `adapters/svg.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `adapters/web.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `adapters/doc.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |
| `adapters/generic.py: _smoke()` | Manual smoke test. Not a pytest test. | [CONFIRMED] |

### 8.5 Known Risks (from regression notes)

| Risk | Status | Mitigation |
|------|--------|-----------|
| Pi writes outside workspace | Mitigated | `PiClient._path_is_outside_workspace()`, `Workspace.reconcile_external_writes()` |
| Large SVG truncation | Mitigated | Generator-first workflow (`generate_artifact.py`) |
| Read-only Pi turns | Mitigated | Pre-write tool budget, no-write timeout, retry prompt |
| Planner rewrites spec | Mitigated | `_preserves_spec()`, `_retarget_spec_edit_intent()` |
| Judge misses structural defects | Mitigated | Two-pass design, position/spatial guards |
| `.env` not gitignored | Risk | `.env` is tracked in repo with plaintext API keys |

### 8.6 Verification Needs

| Item | How to Verify |
|------|--------------|
| `agno` version 2.6.4 API compatibility | `pip show agno` + check `agno.agent.Agent` constructor signature |
| `playwright` chromium installation | `playwright install chromium` |
| `pi` binary availability | `which pi` + `pi --version` |
| LiteLLM proxy connectivity | `curl $LITELLM_BASE_URL/models` |
| `THELOOP_MODEL_CODER` override in `.env` | Check `.env` — currently set to `Qwen3.6-Mesh-Thinking-Long` (differs from default `Qwen3.6-Mesh-Code-Long`) |
| `docs/env-management.md` content | Read file (not yet examined) |
| `examples/primes.spec.md` content | Read file (not yet examined) |
| `examples/improve-spec.spec.md` content | Read file (not yet examined) |
| `.claude/settings.local.json` content | Read file (not yet examined) |
| `tests/start.sh` content | Read file (not yet examined) |

[CONFIRMED]

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Source files (src/theloop/) | 16 |
| Test files | 4 |
| Prompt templates | 4 |
| Example specs | 6 |
| Total source lines (est.) | ~3,500 |
| Total test lines (est.) | ~300 |
| External dependencies | 8 direct, ~30 transitive |
| LLM model aliases | 6 (Hat enum) |
| Task adapters | 4 (svg, web, doc, generic) |
| Git branches per run | 1 (main) + N (iter/0..N-1) |
| Test coverage (pytest) | ~30% of source (4 focused test files) |
| CI/CD | None |
| Linter/formatter | None |
| Secrets in repo | Yes (`.env` with API keys) |

---

*End of repository map.*
