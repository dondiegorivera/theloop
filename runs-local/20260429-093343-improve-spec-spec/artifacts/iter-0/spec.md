---
adapter: doc
source: ../docs/spec.md
max_iters: 4
score_threshold: 0.9
no_improvement_for: 3
---

# TheLoop System Specification

## §1 Overview
TheLoop is a closed-loop agentic architecture that iteratively refines artifacts through structured critique and generation. It operates as a single orchestrator system delegating specialized tasks to role-based hats, driven by a code-writer component and managed by an orchestration framework.

## §2 Core Terminology
- **Adapter**: A pluggable interface that standardizes how the system reads, writes, and evaluates artifacts. Four types exist: `doc`, `code`, `data`, and `config`.
- **Hat**: A specialized role or sub-agent assigned a single responsibility (e.g., Critic Hat, Writer Hat).
- **Render**: The process of transforming structured data or prompts into final output formats.
- **Judge**: The evaluation component that scores artifacts against a rubric and provides structured critique.
- **pi**: The code-writer component responsible for generating and modifying implementation artifacts.
- **agno**: The underlying orchestrator framework that manages state, routing, and hat delegation.
- **LiteLLM**: A proxy layer that standardizes API calls across multiple LLM providers.
- **Mesh**: The internal communication bus connecting hats, the judge, and the orchestrator.

## §3 Architecture Principles
The system enforces a single-orchestrator topology to prevent state divergence. All hats communicate through the mesh, and the judge operates as a deterministic scoring layer. Vision feedback is routed through headless Chromium to capture UI/render states before critique. See §4 for the full component breakdown.

## §4 Components
1. **Orchestrator Manager.** The central control plane that initializes sessions, routes tasks to hats, and enforces phase boundaries.
2. **Hat Dispatcher.** Assigns incoming requests to specialized hats based on adapter type and task metadata.
3. **Code Writer (pi).** Generates and refines implementation files, ensuring syntax validity and framework alignment.
4. **Critic Hat.** Evaluates artifacts against rubrics, identifies structural defects, and outputs structured critique.
5. **Vision Feedback Module.** Uses headless Chromium to render and capture UI states, converting them to vision tokens for the judge.
6. **LLM Proxy (LiteLLM).** Normalizes model routing, rate limiting, and fallback strategies across providers.

## §5 Configuration & Routing
Routing rules are defined in YAML frontmatter and resolved at session start. The `adapter` field dictates which hat pipeline is activated. Cross-references between sections are validated during initialization to prevent broken links. See §8 for configuration examples.

## §6 Evaluation & Feedback Loop
The judge scores artifacts using a weighted rubric. Each fully satisfied criterion adds to the score; each miss subtracts. Critique is appended to the iteration history and fed back to pi for the next cycle. See §11 for tracked open items.

## §7 Error Handling & Fallbacks
Failed hat executions trigger automatic retries with adjusted prompts. If the judge score remains below `score_threshold` after `max_iters`, the session terminates and logs the final artifact state.

## §8 Concrete Examples
```yaml
adapter: doc
source: ../docs/spec.md
max_iters: 4
score_threshold: 0.9
no_improvement_for: 3
```
```bash
theloop init --adapter doc --source docs/spec.md
theloop run --max-iters 4 --threshold 0.9
```

## §9 CLI & API Specs
The CLI exposes `init`, `run`, `score`, and `critique` commands. All commands accept `--adapter` and `--source` flags. API endpoints mirror CLI flags and return JSON payloads containing rubric scores and critique blocks.

## §10 Deployment & Infrastructure
The system runs headlessly in containerized environments. LiteLLM proxy is deployed as a sidecar. Headless Chromium is allocated via Docker with GPU passthrough for vision rendering.

## §11 Open Items
- [§4.4] Critic Hat scoring weights need explicit normalization across adapter types.
- [§6] Judge critique format should support structured JSON output for programmatic parsing.
- [§8] CLI examples require explicit environment variable setup instructions for LiteLLM proxy.

## Iteration history
- iter 0: Established initial structural scaffold with all rubric-referenced sections (§4–§11) and defined core terminology → enables meaningful first-pass scoring against clarity and consistency rubric.