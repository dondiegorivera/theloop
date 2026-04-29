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
2. **Cross-references resolve.** Every reference between sections (e.g.
   "see §4.6") points at a section that actually says what the
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
