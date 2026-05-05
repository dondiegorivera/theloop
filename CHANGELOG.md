# Changelog

## 2026-05-05 - Prose adapter foundation

Branch: `feature/prose-adapter-foundation`

This checkpoint starts the typed-artifact sprint from
`docs/sprint-typed-artifact-loop-2026-05-05.md`. The goal is to move writing
tasks away from the broad `generic` adapter and into a first-class prose path
with a canonical artifact, deterministic checks, and prose-specific judging.

### Implemented

- Added `adapter: prose`.
  - New file: `src/theloop/adapters/prose.py`
  - Registered in `src/theloop/adapters/__init__.py`.
  - Default artifact is `artifact.md`.
  - Supports frontmatter:
    - `artifact`
    - `target_words`
    - `word_tolerance`
    - `banned_phrases`
    - `required_prefix`
  - Runtime checks now catch:
    - missing artifact
    - empty artifact
    - unchanged scaffold placeholder
    - word count outside tolerance
    - banned phrases, case-insensitive
    - missing required prefix
  - `artifact_text()` exposes only the canonical prose artifact to the judge.

- Added adapter-level judge profiles.
  - New default method: `TaskAdapter.judge_profile()`.
  - Visual adapters default to `visual_presence`.
  - Non-visual adapters default to `text_presence`.
  - `ProseAdapter` overrides this as `prose_quality`.
  - `Loop` emits the profile in `judge_start` and passes it to `Judge.evaluate()`.

- Added prose-specific judge prompts.
  - `src/theloop/prompts/judge_describe_prose.md`
  - `src/theloop/prompts/judge_prose.md`
  - Prose describe prompt extracts hard constraints and craft observations.
  - Prose verdict prompt returns hard failures, dimension scores, critique,
    done flag, and next action.

- Extended `JudgeVerdict`.
  - Added optional structured fields:
    - `hard_failures`
    - `dimensions`
    - `next_action`
    - `regression_against_best`
  - Existing `{score, critique, done}` JSON still parses.
  - For `prose_quality`, hard failures force `done=false`.

- Persisted richer artifacts and verdicts.
  - Text artifacts are written to `artifacts/iter-N/artifact.txt`.
  - Structured verdicts are written to `artifacts/iter-N/verdict.json`.
  - No-op/reused-verdict iterations also persist the current text artifact.

- Improved the HTML report for text/prose runs.
  - Links `artifacts/iter-N/artifact.txt` as the judged artifact.
  - Displays hard failures when present.
  - Displays dimension scores when present.

- Improved `generic`.
  - `generic` now exposes text-like files to the judge instead of relying only
    on Pi's final assistant message.
  - This fixes runs where Pi produced `scene.txt` but the judge saw
    `(no artifact provided)`.

- Added prose example.
  - `examples/the-trip.prose.md`
  - Uses `adapter: prose`, `artifact: scene.md`, `target_words: 200`, and
    `word_tolerance: 20`.

- Updated README.
  - Added `prose` to the adapter list and CLI examples.
  - Recommends `prose` for new writing tasks.
  - Clarifies that `generic` is the fallback for tasks without a stronger
    artifact contract.

### Tests Added

- `tests/test_prose_adapter.py`
  - Adapter registration.
  - Configured artifact path.
  - Placeholder rejection.
  - Word-count pass/fail.
  - Banned phrase detection.
  - Required prefix checks.
  - Invalid frontmatter rejection.
  - Judge profile defaults.

- `tests/test_generic_adapter.py`
  - Text-like generic outputs are exposed to the judge.
  - Scaffold README is excluded.

- `tests/test_reporter.py`
  - Report links judged text artifacts.
  - Report renders hard failures and dimension scores.

- Existing judge and loop tests were extended for:
  - backward-compatible verdict parsing
  - prose structured verdict parsing
  - verdict payload persistence fields

### Verification

Latest local verification:

```text
.venv/bin/python -m pytest
51 passed

.venv/bin/python -m compileall src/theloop
ok
```

### Current State

The repo now has a runnable prose foundation. A writing task can use:

```yaml
adapter: prose
artifact: scene.md
target_words: 200
word_tolerance: 20
```

This gives the loop a canonical artifact file, deterministic runtime checks,
prose-specific judge prompts, structured judge output, and better reports.

This is not the full SOTA loop yet. The biggest missing pieces are still:

- best-so-far tracking
- pairwise prose comparison against best-so-far
- `memory.md` run memory
- report-level best artifact link
- candidate branching
- `code` adapter with test-command validation

### Next Recommended Step

Implement best-so-far tracking and pairwise prose comparison:

1. Persist `runs/<id>/best/artifact.txt`.
2. Persist `runs/<id>/best/verdict.json`.
3. Add `Judge.compare()` with `judge_compare_prose.md`.
4. On prose iter 1+, compare current candidate against best-so-far.
5. If the candidate regresses, keep the iteration for traceability but do not
   replace the best artifact and force `done=false`.
