# theloop — Repository Map (Sections 1–2)

## 1. 📁 REPOSITORY STRUCTURE

```
theloop/
├── .env                          # ⚙️ config — env vars (LITELLM_BASE_URL, LITELLM_MASTER_KEY, PI_CODING_AGENT_DIR, THELOOP_MODEL_CODER)
├── .gitignore                    # ⚙️ config — excludes .venv/, runs/, .pytest_cache/, *.pyc, etc.
├── .claude/settings.local.json   # ⚙️ config — Claude Code project settings
├── .codex                        # ⚙️ config — Codex project config (image)
├── CLAUDE.md                     # ⚙️ config — Claude Code agent instructions (pre-code state note, Python venv, LiteLLM model roles)
├── README.md                     # 📖 doc — user-facing overview, quick start, architecture diagram, spec format, CLI docs
├── pyproject.toml                # 📦 build — uv/pip project manifest (hatchling build, theloop package, CLI entry point)
├── requirements.txt              # 📦 build — full pip freeze of the venv (50+ pinned deps)
├── uv.lock                       # 📦 build — uv lockfile (deterministic resolution)
├── claude.log                    # 📝 log — Claude Code session log (auto-generated)
│
├── src/theloop/                  # 📚 lib — theloop package (src-layout)
│   ├── __init__.py               # 📦 init — loads .env on import, defines __version__
│   ├── __main__.py               # 🚪 entry — `python -m theloop` → calls cli:app()
│   │
│   ├── cli.py                    # 🚪 entry — Typer CLI: `run <spec.md>` + `report <run_dir>`
│   ├── loop.py                   # 🧩 core — Loop class: main async control flow (plan→direct→pi→check→render→judge→commit)
│   ├── orchestrator.py           # 🧩 core — Orchestrator: agno Agents (planner + director hats)
│   ├── pi_client.py              # 🧩 core — PiClient: async subprocess wrapper around `pi --mode rpc`
│   ├── renderer.py               # 🧩 core — Renderer: async Playwright Chromium screenshot wrapper
│   ├── judge.py                  # 🧩 core — Judge: two-pass evaluation (describe → verdict)
│   ├── terminator.py             # 🧩 core — Terminator: composite stop condition (done/threshold/plateau/max_iters)
│   ├── workspace.py              # 🧩 core — Workspace: per-run git repo, branch-per-iteration
│   ├── reporter.py               # 🧩 core — Reporter: JSONL event log + static HTML report builder
│   ├── models.py                 # 🧩 core — Hat enum, alias resolution, LiteLLM config loader
│   │
│   ├── adapters/                 # 🧩 lib — TaskAdapter registry + implementations
│   │   ├── __init__.py           # 📦 init — ADAPTERS dict, get_adapter(), __all__ exports
│   │   ├── base.py               # 📐 abc — TaskAdapter ABC + RuntimeCheckResult
│   │   ├── svg.py                # 🎨 adapter — SVG task: XML parse check, Chromium screenshot of inline SVG
│   │   ├── web.py                # 🌐 adapter — Web app: HTML parse check, Chromium screenshot with __ready signal
│   │   ├── doc.py                # 📄 adapter — Doc improvement: source copy, text-only judge, context/ reference material
│   │   └── generic.py            # 📦 adapter — Generic catch-all: no render, text judge against spec + assistant turn
│   │
│   └── prompts/                  # 📝 config — Markdown prompt templates per role
│       ├── planner.md            # 📝 prompt — Planner role: spec evolution + iteration intent
│       ├── director.md           # 📝 prompt — Director role: intent → concrete pi prompt
│       ├── judge.md              # 📝 prompt — Judge verdict pass: weighted scoring formula
│       └── judge_describe.md     # 📝 prompt — Judge describe pass: PRESENT/PARTIAL/HIDDEN/MISSING classification
│
├── tests/                        # 🧪 test — pytest test suite
│   ├── start.sh                  # 🧪 test — Test runner script
│   ├── test_judge_scoring.py     # 🧪 test — Judge scoring, description guards, position/spatial guards
│   ├── test_loop_retry_prompt.py # 🧪 test — Retry prompt constraints, pre-write policy
│   ├── test_orchestrator_plan.py # 🧪 test — Planner spec preservation, intent coercion, anti-pattern rejection
│   └── test_workspace_reconcile.py # 🧪 test — External write reconciliation
│
├── examples/                     # 📖 example — Working spec files for all adapters
│   ├── pelican.spec.md           # 📖 example — SVG: pelican on bicycle
│   ├── watch.spec.md             # 📖 example — SVG: mechanical pocket watch (detailed)
│   ├── robot.md                  # 📖 example — SVG: Victorian robot in cafe
│   ├── dragon-flappy.spec.md     # 📖 example — Web: 3D flappy-bird game
│   ├── primes.spec.md            # 📖 example — (content not read)
│   └── improve-spec.spec.md      # 📖 example — (content not read)
│
├── docs/                         # 📖 doc — Design docs, spec, regression notes
│   ├── spec.md                   # 📖 doc — System specification (v1): architecture, components, model roles, phase plan
│   ├── litellm-endpoints.md      # 📖 doc — LiteLLM config.yaml variants (35B vs 27B backbones)
│   ├── agno.md                   # 📖 doc — agno vendor docs (pasted)
│   ├── pi.md                     # 📖 doc — pi vendor docs (pasted, 13KB+)
│   ├── env-management.md         # 📖 doc — (content not read)
│   ├── regression-recovery-2026-05-01.md # 📖 doc — Post-mortem of visual SVG regressions + fixes applied
│   └── map/                      # 📖 doc — Repository map output
│       └── 00-map.md             # 📖 doc — Prompt template (previous iteration's prompt)
│
└── runs/                         # 🗂️ data — Generated per-run output (gitignored)
    ├── <run-id>/                 # Each run: workspace/ + artifacts/iter-N/ + events.jsonl + index.html
    │   ├── workspace/            # Git repo with iter/N branches
    │   ├── artifacts/            # Per-iteration artifacts (render.png, judge_description.txt, pi_prompt.txt, etc.)
    │   ├── events.jsonl          # Append-only event log
    │   └── index.html            # Static HTML report
```

### Build Tools & Package Management

| Tool | Role | Evidence |
|------|------|----------|
| **uv** | Primary package manager | `pyproject.toml` → `[tool.uv]`, `uv.lock` exists |
| **hatchling** | Build backend | `pyproject.toml` → `[build-system]` |
| **pip** | Fallback (requirements.txt present) | `requirements.txt` with full freeze |
| **pytest** | Test runner | `pyproject.toml` dev deps, `tests/` directory |
| **typer** | CLI framework | `pyproject.toml` deps, `cli.py` uses `typer.Typer` |
| **agno** | Agent orchestration | `pyproject.toml` deps, `orchestrator.py` uses `agno.agent.Agent` |
| **playwright** | Headless browser | `pyproject.toml` deps, `renderer.py` uses `playwright.async_api` |
| **GitPython** | Git operations | `pyproject.toml` deps, `workspace.py` uses `git.Repo` |
| **pydantic** | Data validation | `pyproject.toml` deps, `orchestrator.py` uses `pydantic.BaseModel` |
| **python-dotenv** | Env loading | `pyproject.toml` deps, `__init__.py` calls `load_dotenv()` |

**No CI/CD files detected.** No linter/formatter config (no `.pre-commit-config.yaml`, `ruff.toml`, `pyproject.toml` `[tool.ruff]`, etc.).

[CONFIRMED]

---

## 2. 🚪 ENTRY POINTS & EXECUTION FLOW

### 2.1 CLI Entry Points

| Entry Point | Invocation | File | Description |
|-------------|-----------|------|-------------|
| `python -m theloop` | `__main__.py` | `src/theloop/__main__.py` | Calls `cli.app()` — same as `theloop` script |
| `theloop` | pip script | `pyproject.toml` → `[project.scripts]` | Typer app entry: `theloop = "theloop.cli:app"` |
| `python -m theloop run <spec>` | CLI command | `src/theloop/cli.py` → `run()` | Main loop execution |
| `python -m theloop report <dir>` | CLI command | `src/theloop/cli.py` → `report()` | Regenerate HTML report from existing run |

### 2.2 Package-Level Entry

| Entry | File | Description |
|-------|------|-------------|
| `import theloop` | `src/theloop/__init__.py` | Loads `.env` from project root on first import |

### 2.3 Module-Level Smoke Tests (manual)

Each module has an `if __name__ == "__main__"` block with a `_smoke()` function:

| Module | Smoke Test |
|--------|-----------|
| `models.py` | Prints LiteLLM config + hat→alias mapping |
| `orchestrator.py` | Round-trips `plan()` + `direct()` against live proxy |
| `judge.py` | Runs vision probe + `evaluate()` on placeholder SVG |
| `pi_client.py` | Spawns `pi --mode rpc`, sends "PONG" prompt |
| `renderer.py` | Renders a test SVG to PNG via Playwright |
| `workspace.py` | Creates run, commits iter 0/1, verifies branches + diff |
| `reporter.py` | Writes events, verifies JSONL output |
| `terminator.py` | Tests all stop-condition combinations |
| `adapters/svg.py` | Full SVG adapter lifecycle (scaffold → check → render → break) |
| `adapters/web.py` | Web adapter lifecycle + `__ready` fallback |
| `adapters/generic.py` | Runtime check on empty vs populated workspace |
| `adapters/doc.py` | Doc adapter configure/prepare/runtime_check |

### 2.4 Execution Flow: `theloop run <spec.md>`

```
cli:run()
  │
  ├─ 1. Parse spec: YAML frontmatter + markdown body
  │     └─ _parse_frontmatter() → (fm, body)
  │     └─ _normalize_spec_text() → compacted spec
  │
  ├─ 2. Resolve adapter: frontmatter["adapter"] or --adapter flag
  │     └─ get_adapter(name) → TaskAdapter instance
  │     └─ adapter.configure(fm, spec_path)
  │
  ├─ 3. Build TerminationConfig from frontmatter or CLI overrides
  │
  ├─ 4. Create Workspace: runs/<run_id>/workspace/ (git init)
  │
  ├─ 5. Create Judge + vision_probe() (if adapter has visual artifact)
  │
  ├─ 6. Create Orchestrator (planner + director agno Agents)
  │
  ├─ 7. Create Reporter (events.jsonl writer)
  │
  ├─ 8. Create Loop (all components wired)
  │     │
  │     └─ Loop.run()  ← main async loop
  │           │
  │           ├─ iter 0:
  │           │   ├─ workspace.begin_iteration(0) → checkout main
  │           │   ├─ adapter.prepare(workspace) → scaffold files
  │           │   ├─ for it in range(max_iters):
  │           │   │   ├─ orchestrator.plan(spec, critique) → PlanResult(spec, intent)
  │           │   │   ├─ orchestrator.direct(intent, ws, adapter_notes) → pi_prompt
  │           │   │   ├─ pi_client.prompt(pi_prompt) → PiResult
  │           │   │   ├─ workspace.reconcile_external_writes(touched)
  │           │   │   ├─ adapter.runtime_check(workspace) → RuntimeCheckResult
  │           │   │   ├─ adapter.render(workspace, png) → render.png (if visual)
  │           │   │   ├─ judge.evaluate(spec, png, pi_text) → JudgeVerdict
  │           │   │   ├─ workspace.commit_iteration(it, intent) → sha
  │           │   │   └─ terminator.should_stop(history) → StopReason | None
  │           │   └─ if stop: break
  │           └─ return RunResult
  │
  └─ 9. build_html_report(run_dir) → index.html
```

### 2.5 Per-Iteration Flow (detailed)

```
_loop._run_one(iter, spec, critique, description, verdict)
  │
  ├─ 1. plan_start event
  ├─ 2. orchestrator.plan(spec, critique, description)
  │     ├─ planner Agent.arun(user_prompt) → raw JSON
  │     └─ _parse_plan(raw) → PlanResult(spec, intent)
  │         ├─ _normalize_markdown() — compact spec
  │         ├─ _preserves_spec(candidate, fallback) — reject rewritten specs
  │         └─ _retarget_spec_edit_intent() — convert "update spec" → "fix artifact"
  │
  ├─ 3. direct_start event
  ├─ 4. orchestrator.direct(spec, intent, workspace, adapter_notes)
  │     ├─ _workspace_inventory(workspace) → file listing
  │     ├─ director Agent.arun(user_prompt) → raw text
  │     └─ _compose_pi_prompt(spec, directive) → final pi prompt
  │
  ├─ 5. pi_start event
  ├─ 6. _run_pi_with_retry(iter, prompt)
  │     ├─ _run_pi(iter, prompt, attempt=0)
  │     │   ├─ pi.new_session()
  │     │   ├─ pi.prompt(prompt, on_event=on_event, timeout=600s)
  │     │   │   ├─ heartbeat() — no-write timeout (120s default)
  │     │   │   ├─ on_event() — pre-write policy check
  │     │   │   └─ live log: pi_live.log
  │     │   └─ return PiResult
  │     └─ TimeoutError → retry with _compose_pi_retry_prompt()
  │         └─ _run_pi(iter, retry_prompt, attempt=1)
  │
  ├─ 7. pi_end event
  ├─ 8. workspace.reconcile_external_writes(touched)
  │
  ├─ 9. adapter.runtime_check(workspace) → RuntimeCheckResult
  │
  ├─ 10. adapter.render(workspace, png) → render.png (if visual + rc.ok)
  │
  ├─ 11. judge.evaluate(spec, png, pi_text, artifact_text)
  │     ├─ _describe(png, artifact_text, spec) → description
  │     │   ├─ vision path: JUDGE_VISION alias + base64 image
  │     │   └─ text path: JUDGE_TEXT alias + trimmed artifact text
  │     └─ verdict call: JUDGE_TEXT alias → JSON verdict
  │
  ├─ 12. judge_end event
  ├─ 13. workspace.commit_iteration(iter, intent) → sha
  │
  └─ 14. terminator.should_stop(history) → StopReason | None
```

[CONFIRMED]

---

*Continued in: `02-modules-and-data-flow.md`*
