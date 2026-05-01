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

# Improve theloop's own system specification

Improve `document.md` (a copy of `docs/spec.md`) for clarity, internal
consistency, and completeness. Score against this rubric — every bullet
that fully holds adds to the score, every miss subtracts:

1. **Single responsibility.** Every component in §4 has one clear
   responsibility, named in its first sentence.
2. **Cross-references resolve.** Every reference between sections (e.g. "see §4.6") points at a section that actually says what the
   reference implies.
3. **No undefined terms.** Domain jargon (hat, adapter, render, judge, pi, agno, LiteLLM, alias, mesh) is introduced before first use.
4. **Concrete, copy-pasteable examples.** Code/CLI/spec examples in §8 and §9 should be copy-pasteable; placeholders are clearly marked.
5. **Open items are scoped.** §11 entries are tagged with the section they affect (e.g. "[§4.6] Critic hat …").

Hard constraints — do **not** change:
- Architectural decisions (single orchestrator with hats, pi as code writer, agno as orchestrator framework, LiteLLM proxy, headless Chromium for vision feedback).
- Frontmatter conventions or the four adapter types.
- Phase-1 vs phase-2 split.

Refine wording, fill gaps, fix inconsistencies. Add cross-references
where they would help a reader. Append an `## Iteration history`
section at the end if you want to track what changed across iterations
(the planner appends to it automatically).

## 1. Introduction

This document specifies the architecture and operational procedures of theloop, a closed agentic loop system for automated software development and specification refinement. The system uses an orchestrator framework to coordinate specialized agents ("hats") that perform distinct roles in the development lifecycle.

## 2. Terminology

- **agno**: The orchestrator framework used to manage agent state and communication.
- **pi**: The code-writing agent responsible for implementing changes.
- **Judge**: The component or agent responsible for evaluating outputs against a rubric.
- **Hat**: A role assigned to an agent, defining its specific responsibility (e.g., Critic, Renderer).
- **Adapter**: A component that interfaces with external services or data sources.
- **LiteLLM**: A proxy service used to standardize API calls to various LLM endpoints.
- **Mesh**: The network of connections between agents and services.
- **Alias**: A shorthand reference to a specific agent or component configuration.

## 3. Architecture Overview

The system follows a single orchestrator pattern where agno manages the flow of tasks. Agents operate under hats, each with a single responsibility. The system integrates with LiteLLM for model inference and uses headless Chromium for vision-based feedback.

## 4. Components

### 4.1. Orchestrator (agno)

The orchestrator manages the state machine of the agentic loop, dispatching tasks to hats and aggregating results.

### 4.2. Code Writer (pi)

pi is the agent responsible for generating and modifying source code based on instructions from the orchestrator.

### 4.3. Judge

The judge evaluates the output of pi against a defined rubric, providing feedback for iteration.

### 4.4. Renderer

The renderer converts internal representations into human-readable formats, such as HTML or Markdown.

### 4.5. Critic Hat

The critic hat analyzes outputs for logical consistency and adherence to constraints, providing corrective feedback.

### 4.6. Vision Feedback Agent

This agent uses headless Chromium to capture screenshots and provide visual feedback on UI-related tasks.

## 5. Workflows

### 5.1. Iteration Loop

The core loop involves pi generating code, the judge evaluating it, and the orchestrator deciding whether to iterate or finalize.

### 5.2. Specification Refinement

This workflow focuses on improving system specifications using the same agentic loop, ensuring clarity and completeness.

## 6. Configuration

Configuration is managed via environment variables and YAML files. The LiteLLM proxy URL is set in `.env` as `LITELLM_BASE_URL`.

## 7. Integration

The system integrates with upstream llama.cpp endpoints via LiteLLM. Context files are loaded from `../src/theloop` and `../docs/litellm-endpoints.md`.

## 8. Examples

### 8.1. CLI Usage

```bash
python main.py --mode refine --spec docs/spec.md
```

### 8.2. API Call

```python
response = litellm.completion(
    model="gpt-4",
    messages=[{"role": "user", "content": "Refine this spec."}]
)
```

## 9. Deployment

Deploy the system using Docker, ensuring environment variables are set. The LiteLLM proxy must be running and accessible.

## 10. Troubleshooting

- **API Errors**: Check `LITELLM_BASE_URL` and network connectivity.
- **Vision Failures**: Ensure headless Chromium is installed and accessible.

## 11. Open Items

- [§4.5] Define specific criteria for the Critic hat's feedback.
- [§8.2] Add error handling examples for API calls.

## Iteration history

- iter 0: Drafted the core system description including components like pi, agno, and the hat architecture, ensuring terms are defined and responsibilities are clear, to establish the baseline content for the specification. → Provided a complete specification body with defined terms, single-responsibility components, and concrete examples.