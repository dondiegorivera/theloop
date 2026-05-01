---
adapter: doc
source: ../docs/spec.md
context:
  - ../src/theloop
  - ../docs/litellm-endpoints.md
context_notes: |
  - The LiteLLM proxy URL is in `.env` as `LITELLM_BASE_URL`. The
    `api_base` lines inside `context/litellm-endpoints.md` are the
    *upstream* llama.cpp endpoints that LiteLLM forwards *to*, NOT
    the proxy URL the rest of the project talks to.
  - When citing function signatures, file paths, or class names,
    grep `context/theloop/` first; do not rely on memory.
  - Do not invent class members (e.g. `JudgeVerdict` fields,
    `RuntimeCheckResult` fields) — they are defined in `context/theloop/`.
max_iters: 4
score_threshold: 0.9
no_improvement_for: 3
---

# The Loop System Specification

## §1 Introduction
This document defines the architecture, components, and operational phases of **The Loop**, a closed agentic system for iterative software development and documentation refinement. It serves as the single source of truth for agent behavior, adapter routing, and evaluation criteria.

## §2 Architecture Overview
The system follows a single-orchestrator pattern where the orchestrator manages the high-level state machine. Agents operate under specialized **hats** that constrain their prompt context. Communication flows through a typed **mesh** of **adapters** that translate internal state to LLM API calls via a **LiteLLM** proxy. Visual feedback is captured using **headless Chromium** and routed to the vision pipeline.

## §3 Terminology
All domain jargon is introduced here before first use in subsequent sections:
- **Hat**: A prompt wrapper that enforces a single behavioral constraint or role (e.g., `CriticHat`, `WriterHat`).
- **Adapter**: A routing module that translates structured messages to external APIs. Four types exist: `code`, `doc`, `vision`, and `tool`.
- **Render**: The serialization process that converts internal state objects into prompt-ready text or JSON payloads.
- **Judge**: The evaluation component that compares agent outputs against a scoring rubric and returns a verdict.
- **Code Writer**: The dedicated agent responsible for generating, refactoring, and validating source files.
- **Orchestrator**: The framework that manages the agent loop, state persistence, and tool execution.
- **LiteLLM**: A standardized proxy server that normalizes API calls across different LLM providers.
- **Alias**: A configuration shorthand mapping a logical name to a specific model endpoint or adapter type.
- **Mesh**: The underlying message-passing network connecting adapters, agents, and the orchestrator.

## §4 Components & Responsibilities
Each component below has exactly one primary responsibility, named in its first sentence.

### §4.1 Orchestrator
The orchestrator manages the high-level execution loop, state persistence, and agent coordination.
### §4.2 Hat Manager
The hat manager instantiates, caches, and switches between specialized prompt templates based on the current phase and task type.
### §4.3 Adapter Registry
The adapter registry routes requests to the correct adapter type (`code`, `doc`, `vision`, `tool`) and handles LiteLLM proxy communication.
### §4.4 Judge Verifier
The judge verifier evaluates agent outputs against scoring rubrics and returns pass/fail verdicts with actionable feedback.
### §4.5 Vision Feedback Service
The vision feedback service uses headless Chromium to capture UI screenshots and feeds them back to the vision adapter for visual grounding.

## §5 Phases & Split
Development is divided into two distinct phases to manage complexity and verify foundational stability.
- **Phase 1**: Core loop setup, adapter wiring, and basic hat routing. Focuses on getting the code writer and orchestrator communicating reliably.
- **Phase 2**: Advanced vision feedback, judge rubric integration, and multi-agent mesh expansion. Focuses on closing the loop with visual grounding and automated scoring.

## §6 Hard Constraints
The following architectural decisions are fixed and must not be altered:
- Single orchestrator with hats architecture.
- Code writer as the exclusive code generation agent.
- Orchestrator framework as the central control plane.
- LiteLLM proxy for API standardization.
- Headless Chromium for vision feedback.
- Phase-1 vs phase-2 split.
- Four adapter types (`code`, `doc`, `vision`, `tool`).

## §7 Implementation Examples
All examples below are copy-pasteable and use clearly marked placeholders where dynamic values are required.

### §7.1 CLI Startup
```bash
agno run --config config.yaml --phase 1 --adapter code
```

### §7.2 Adapter Configuration
```yaml
adapters:
  - type: code
    alias: main-code
    api_base: ${LITELLM_BASE_URL}/v1/chat/completions
    model: llama.cpp-70b
```

### §7.3 Judge Verdict Payload
```json
{
  "verdict": "PASS",
  "score": 0.92,
  "feedback": "Cross-references in §4 resolve correctly. Terminology matches §3.",
  "failed_criteria": []
}
```

## §8 Open Items
All open items are explicitly scoped to the section they affect to prevent scope creep.
- `[§4.3]` Define timeout behavior for Adapter Registry when LiteLLM proxy is unreachable.
- `[§7.2]` Standardize `api_base` placeholder format across all adapter configs.
- `[§5]` Clarify handoff criteria between Phase 1 and Phase 2.

## Iteration History
- iter 0: Draft the first pass of the improved system specification by explicitly defining all domain jargon, clarifying component responsibilities, and resolving cross-references → a clearer, internally consistent spec ready for scoring.