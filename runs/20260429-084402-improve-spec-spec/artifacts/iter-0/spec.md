---
adapter: doc
source: ../docs/spec.md
max_iters: 4
score_threshold: 0.9
no_improvement_for: 3
---

# Improve theloop's own system specification

Improve `document.md` (a copy of `docs/spec.md`) for clarity, internal
consistency, and completeness. Score against this rubric — every bullet
that fully holds adds to the score, every miss subtracts:

1. **Single responsibility.** Every component in §4 has one clear
   responsibility, named in its first sentence.
2. **Cross-references resolve.** Every reference between sections (e.g. "see §4.6") points at a section that actually says what the
   reference implies.
3. **No undefined terms.** Domain jargon (hat, adapter, render, judge,
   pi, agno, LiteLLM, alias, mesh) is introduced before first use.
4. **Concrete, copy-pasteable examples.** Code/CLI/spec examples in §8
   and §9 should be copy-pasteable; placeholders are clearly marked.
5. **Open items are scoped.** §11 entries are tagged with the section
   they affect (e.g. "[§4.6] Critic hat …").

Hard constraints — do **not** change:
- Architectural decisions (single orchestrator with hats, pi as code
  writer, agno as orchestrator framework, LiteLLM proxy, headless
  Chromium for vision feedback).
- Frontmatter conventions or the four adapter types.
- Phase-1 vs phase-2 split.

Refine wording, fill gaps, fix inconsistencies. Add cross-references
where they would help a reader. Append an `## Iteration history`
section at the end if you want to track what changed across iterations
(the planner appends to it automatically).

## §1 Architecture Overview
The system operates as a single orchestrator loop that delegates specialized tasks to modular hats. The orchestrator framework manages state and execution flow. Code generation is handled by a dedicated code-writing agent. External LLM calls are routed through a unified proxy for interface compatibility. Vision feedback is provided by a headless browser instance that captures and analyzes UI states.

## §2 Component Responsibilities
1. Orchestrator: Manages the execution loop, state persistence, and task routing.
2. Code Writer: Generates, refines, and validates source code based on orchestrator directives.
3. Hat Router: Assigns incoming requests to specialized agent hats based on context and capability.
4. Vision Feedback Module: Renders the application in a headless browser, captures screenshots, and extracts DOM state for analysis.
5. LLM Proxy: Normalizes API calls across different model providers and handles rate limiting.

## §3 Execution Phases
Phase 1 focuses on core loop stability, code generation, and basic LLM routing. Phase 2 introduces advanced hat delegation, vision feedback integration, and multi-agent coordination.

## §4 Component Details
### §4.1 Orchestrator
The orchestrator is the central control plane. It initializes the framework, loads configuration, and drives the main execution loop. All task dispatch originates here.

### §4.2 Code Writer
The code writer receives task specifications from the orchestrator. It produces syntactically correct code, runs local validation, and returns artifacts. See §8.1 for a generation example.

### §4.3 Hat Router
The hat router evaluates request metadata and assigns it to the appropriate specialist agent. It maintains a registry of available hats and their capability tags.

### §4.4 Vision Feedback
The vision feedback module launches a headless browser session, navigates to the target URL, and captures DOM snapshots. Results are passed back to the orchestrator for state comparison. See §9.2 for integration steps.

### §4.5 LLM Proxy
The proxy abstracts vendor-specific APIs. It standardizes request payloads, manages API keys, and enforces throughput limits.

## §5 Cross-Reference Map
- §4.1 → §3 (Phase 1 initialization)
- §4.2 → §8.1 (Code generation example)
- §4.4 → §9.2 (Vision feedback integration)
- §4.5 → §2 (Component responsibilities)

## §6 Terminology Glossary
- **Hat:** A specialized agent persona with a narrow scope of expertise.
- **Adapter:** A configuration interface that standardizes component communication.
- **Render:** The process of generating a visual or DOM state snapshot via a headless browser.
- **Judge:** The evaluation component that scores outputs against the rubric.
- **Pi:** The dedicated code-writing agent.
- **Agno:** The underlying orchestrator framework.
- **LiteLLM:** The LLM routing and proxy layer.
- **Alias:** A shorthand identifier for a specific hat or adapter configuration.
- **Mesh:** The internal communication network connecting all components.

## §7 Implementation Notes
Components communicate via a shared message bus. State is persisted in a local JSON store. All external calls are asynchronous.

## §8 Concrete Examples
### §8.1 Code Generation CLI
```bash
theloop generate --task "implement login form" --model pi
```
*Expected output:* A validated `login.tsx` file with accompanying tests.

### §8.2 Configuration YAML
```yaml
orchestrator: agno
proxy: litellm
vision: chromium-headless
hats:
  - name: code-writer
    alias: pi
```

## §9 Integration Steps
1. Initialize the orchestrator framework and load adapter configs.
2. Configure the LLM proxy with provider keys.
3. Launch the headless browser for vision feedback.
4. Start the main orchestrator loop.

## §10 Constraints & Boundaries
- Single orchestrator pattern is mandatory.
- Phase-1 vs Phase-2 split must be preserved.
- Frontmatter conventions remain unchanged.

## §11 Open Items
- [§4.3] Hat routing strategy for dynamic capability discovery needs benchmarking.
- [§4.4] Vision feedback timeout thresholds require environment-specific tuning.
- [§8.2] Alias resolution logic for nested hat configurations is pending specification.

## Iteration history
- iter 0: Drafted initial structural skeleton with defined sections, component responsibilities, glossary, and placeholder examples to establish a baseline for scoring. → Provides scaffolding for rubric evaluation and iterative refinement.