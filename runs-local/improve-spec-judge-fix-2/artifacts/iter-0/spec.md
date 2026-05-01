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

# TheLoop System Specification

## 1. Overview

TheLoop is an agentic orchestration framework built on the **agno** framework. It manages a loop of specialized roles (**hats**) that collaborate to solve complex tasks. The system uses **pi** as the primary code-writing agent and **LiteLLM** as the LLM proxy for model abstraction. Vision feedback is provided via headless **Chromium**.

## 2. Architecture

The system follows a single-orchestrator pattern. The orchestrator manages the state of the loop, delegates tasks to hats, and aggregates results. Communication between components occurs over a **mesh** layer.

### 2.1. Phases

- **Phase 1:** Core orchestration, hat management, and LiteLLM integration.
- **Phase 2:** Advanced vision feedback, mesh optimization, and adaptive routing.

## 3. Components

### 3.1. Orchestrator

The orchestrator is the central controller. It maintains the loop state, schedules hat execution, and handles error recovery. It uses the **agno** framework for agent management.

### 3.2. Hats

Hats are specialized roles assigned to agents. Each hat has a single responsibility, defined in its first sentence. Examples include:
- **Critic Hat:** Evaluates output quality and provides feedback.
- **Coder Hat:** Writes and refines code.
- **Research Hat:** Gathers information from external sources.

### 3.3. Pi

**pi** is the designated code-writing agent. It receives tasks from the orchestrator and produces code artifacts. It interacts with the **mesh** to share code snippets and receive feedback.

### 3.4. LiteLLM Proxy

The system uses **LiteLLM** as an LLM proxy. The proxy URL is configured in `.env` as `LITELLM_BASE_URL`. Upstream endpoints (e.g., llama.cpp) are defined in `context/litellm-endpoints.md` and are *not* directly accessed by the rest of the project.

### 3.5. Chromium Vision

Headless **Chromium** is used for vision feedback. It captures screenshots of the application state and provides them to vision-capable models for analysis.

## 4. Data Structures

### 4.1. JudgeVerdict

The `JudgeVerdict` class represents the output of the evaluation phase. It contains fields for scoring and feedback, as defined in `context/theloop/`.

### 4.2. RuntimeCheckResult

The `RuntimeCheckResult` class represents the outcome of runtime checks. It includes fields for success status and error details, as defined in `context/theloop/`.

## 5. Configuration

### 5.1. Environment Variables

- `LITELLM_BASE_URL`: The URL of the LiteLLM proxy.
- `OPENAI_API_KEY`: API key for OpenAI-compatible models.
- `CHROMIUM_PATH`: Path to the headless Chromium executable.

### 5.2. Mesh Configuration

The **mesh** layer handles inter-agent communication. It supports message passing and event broadcasting. Configuration is managed via YAML files in the `config/` directory.

## 6. Examples

### 6.1. Starting the Loop

To start the loop, run the following command:

```bash
python -m theloop.main --config config/default.yaml
```

### 6.2. Defining a Hat

To define a new hat, create a class inheriting from `BaseHat`:

```python
from theloop.hat import BaseHat

class MyHat(BaseHat):
    def execute(self, task):
        # Hat logic here
        pass
```

## 7. Open Items

- [§3.2] Clarify hat assignment strategy.
- [§5.2] Define mesh message format.
- [§6.1] Add error handling examples.

## Iteration history

- iter 0: Draft the initial system specification for theloop, defining the orchestrator, hats, pi, and agno roles, clarifying LiteLLM and Chromium integration, and providing concrete examples to satisfy the rubric. → Created a structured spec with defined components, cross-references, and examples.