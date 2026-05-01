# theloop — SVG Path Regression Analysis

## Executive Summary

After switching from Claude to Codex, the SVG path is degrading. I've identified **7 concrete problems** in the codebase that explain this regression, ranked by severity. The root cause is a combination of **model alias mismatch**, **prompt bloat**, **judge scoring fragility**, and **pi subprocess fragility**.

---

## Problem 1: Model Alias Mismatch — Pi Uses Wrong Model [CRITICAL]

**Location**: `.env` line 5 vs `src/theloop/models.py` line 27

**The bug** (verified):
```
.env:         THELOOP_MODEL_CODER=Qwen3.6-Mesh-Thinking-Long
models.py:    Hat.CODER: "Qwen3.6-Mesh-Code-Long"   ← default
```

The `.env` overrides `THELOOP_MODEL_CODER` to `Qwen3.6-Mesh-Thinking-Long`. Verified via `python -c "from theloop.models import alias_for, Hat; print(alias_for(Hat.CODER))"` → `Qwen3.6-Mesh-Thinking-Long`.

The Thinking-Long model has:
| Parameter | Thinking-Long (current) | Code-Long (default) | Ratio |
|-----------|------------------------|---------------------|-------|
| `max_tokens` | 16,384 | 32,768 | **50%** |
| `reasoning_budget` | 4,096 | 8,192 | **50%** |
| `max_input_tokens` | 65,536 | 229,376 | **29%** |
| `temperature` | 0.3 | 0.2 | **higher** |

**Impact**: Pi gets **half the output budget**, **half the reasoning budget**, and **29% of the input context** compared to what Code-Long provides. For detailed SVG generation (37KB+ artifacts), this is catastrophic. The model runs out of output tokens mid-generation, producing truncated SVGs that fail XML validation.

**Fix**: Remove the `THELOOP_MODEL_CODER` override from `.env` or change it to `Qwen3.6-Mesh-Code-Long`.

---

## Problem 2: Pi Thinking Forced Off — Wastes Model's Reasoning Budget [HIGH]

**Location**: `src/theloop/cli.py` line 113

```python
pi_thinking: Annotated[
    str | None,
    typer.Option(...),
] = "off",
```

The CLI defaults `--pi-thinking=off`. The comment says:
> "the CLI's default --pi-thinking=off keeps it from spending that budget on reasoning instead of edits."

**The problem**: With `thinking=off`, pi's model (Thinking-Long, due to the `.env` override) receives **zero reasoning budget**. The model must produce code directly without planning. For complex SVGs (mechanical pocket watch with 60 tick marks, 3 sub-dials, gear trains), this means the model generates code without understanding the structure first. The result is incomplete or malformed SVGs.

**Impact**: Pi produces first-pass artifacts that are structurally incomplete. The judge scores them low, the planner picks a fix, but pi's next attempt is also unreasoned. The loop burns iterations on incremental fixes that never converge.

**Fix**: Change the default to `"low"` or `"medium"` for SVG tasks. Or make it adapter-aware: `--pi-thinking=low` for svg/web, `--pi-thinking=off` for doc/generic.

---

## Problem 3: Prompt Bloat — Director Output Exceeds Pi's Context Window [HIGH]

**Location**: `src/theloop/orchestrator.py` `_compose_pi_prompt()` + `src/theloop/cli.py` `_ADAPTER_NOTES["svg"]`

The final pi prompt is assembled from:
1. **Authoritative spec** — full spec markdown (can be 2KB+ for detailed specs like watch.spec.md)
2. **Iteration directive** — director's output (up to 400 words per the prompt template)
3. **Execution rule** — hardcoded paragraph
4. **Adapter notes** — `_ADAPTER_NOTES["svg"]` is **~600 words** of guidance

For the watch spec (2.5KB spec + 400-word directive + 600-word adapter notes + execution rule), the total prompt is **~4KB**. With the Thinking-Long model's 65K input context, this is fine. But with Code-Long's 229K context, it's also fine. The real problem is that **the adapter notes are too verbose** and compete with the spec for the model's attention.

**Impact**: The model gets confused by conflicting instructions. The adapter notes say "edit generate_artifact.py" but the spec says "draw a detailed mechanical pocket watch". The model tries to do both and produces a generator that doesn't match the spec.

**Fix**: Shorten `_ADAPTER_NOTES["svg"]` to 100-150 words. Move detailed guidance into the director prompt template.

---

## Problem 4: Judge Describe Pass Uses Wrong Model for Vision [MEDIUM]

**Location**: `src/theloop/judge.py` `_describe()` + `src/theloop/models.py` line 33

```python
Hat.JUDGE_VISION: "Qwen3.6-Mesh",
```

The JUDGE_VISION alias maps to `Qwen3.6-Mesh`, which has:
| Parameter | Qwen3.6-Mesh (current) | Qwen3.6-Mesh-Thinking (recommended) |
|-----------|------------------------|-------------------------------------|
| `max_tokens` | 2,048 | 4,096 |
| `reasoning_budget` | 0 | 2,048 |
| `temperature` | 0.7 | 1.0 |

**The problem**: The describe pass needs to produce a detailed element-by-element classification (150-500 words per the prompt template). With 2048 max tokens and no reasoning, the model may truncate its description or produce shallow classifications. The verdict pass then scores from incomplete evidence.

**Impact**: The judge misses structural defects because the describe pass didn't have enough tokens to enumerate all elements. The verdict pass scores higher than it should, and the loop terminates early with a subpar artifact.

**Fix**: Change `JUDGE_VISION` to `Qwen3.6-Mesh-Thinking` or `Qwen3.6-Mesh-Thinking-Long` for more output budget and reasoning.

---

## Problem 5: Pre-Write Tool Budget Too Aggressive for Complex SVGs [MEDIUM]

**Location**: `src/theloop/loop.py` lines 28-29

```python
_LATER_ITER_PREWRITE_TOOL_LIMIT = 8
_RETRY_PREWRITE_TOOL_LIMIT = 4
```

**The problem**: For complex SVG fix iterations, pi needs to:
1. Read `generate_artifact.py` (1 tool)
2. Grep for the relevant section (1 tool)
3. Read a specific section with offset/limit (1 tool)
4. Edit the generator (1 tool)
5. Run the generator (1 tool)
6. Verify the output (1 tool)

That's 6 tools before the first write. With a limit of 8, there's only 2 tools of slack. If pi needs to read multiple sections or verify multiple times, it hits the limit and gets retried with a shorter prompt. The retry has a limit of 4, which is even tighter.

**Impact**: Pi gets interrupted mid-fix, retried with a shorter prompt, and produces a worse artifact. The loop burns iterations on retries that don't improve the SVG.

**Fix**: Increase `_LATER_ITER_PREWRITE_TOOL_LIMIT` to 12-15 for SVG tasks. Or make it adapter-aware.

---

## Problem 6: No-Write Timeout Too Short for Complex SVGs [MEDIUM]

**Location**: `src/theloop/cli.py` line 107

```python
pi_no_write_timeout_s: Annotated[
    float,
    typer.Option(...),
] = 120.0,
```

**The problem**: 120 seconds is the default no-write timeout. For complex SVGs, pi needs to:
1. Read the generator (5-10 seconds)
2. Plan the edit (10-30 seconds of reasoning)
3. Make the edit (5-10 seconds)
4. Run the generator (5-10 seconds)
5. Verify the output (5-10 seconds)

That's 30-75 seconds of tool use. With the Thinking-Long model's slower reasoning (4096 token budget), this could easily exceed 120 seconds. The loop cancels the turn and retries with a shorter prompt.

**Impact**: Pi gets interrupted mid-fix, retried with a shorter prompt, and produces a worse artifact. The loop burns iterations on retries that don't improve the SVG.

**Fix**: Increase `--pi-no-write-timeout-s` to 180-240 for SVG tasks. Or make it adapter-aware.

---

## Problem 7: Vision Probe May Fail Silently [LOW]

**Location**: `src/theloop/judge.py` `vision_probe()`

**The problem**: The vision probe sends a 32×32 red PNG and asks for the dominant color. If the model replies with anything other than "red", the probe fails and the judge falls back to text-only mode. The CLI prints `vision: unavailable (text-only fallback)` but doesn't fail the run.

**Impact**: If the vision probe fails, the judge runs in text-only mode. The describe pass sees the SVG source code instead of the rendered image. The verdict pass scores from code analysis instead of visual analysis. The loop may terminate early with a subpar artifact that looks wrong but has correct code.

**Fix**: Make the vision probe more robust. Retry with a larger image. Log a warning if the probe fails.

---

## Additional Observations

### The `.env` File Has a Leading Space on Line 5

```
 THELOOP_MODEL_CODER=Qwen3.6-Mesh-Thinking-Long
```

There's a leading space before `THELOOP_MODEL_CODER`. Verified via `cat -A .env` — line 5 starts with a space character. However, `python-dotenv` handles leading whitespace gracefully, so the env var is loaded correctly. This is **not a bug** but a code style issue that could confuse readers.

### The `Hat.WRITER` Enum Value Is Never Used

```python
Hat.WRITER: "Qwen3.6-Mesh-Thinking-Long",
```

The WRITER hat is defined but never used. Doc tasks use CODER instead. This is dead code.

### The `pi_no_workspace_changes` Path Reuses Previous Verdict

```python
if it > 0 and prev_verdict is not None and not ws.repo.git.diff():
    # reuse previous verdict
```

When pi makes no workspace changes, the loop reuses the previous verdict. This is intentional to avoid stochastic re-judging. However, it means that if pi produces a worse artifact (e.g., by editing the generator incorrectly), the loop doesn't detect the regression. The verdict is the same as the previous iteration, and the loop continues with the same critique.

### The Judge's Description Score Guard Can Be Too Aggressive

```python
def _apply_description_score_guard(...):
    desc_score = _score_from_description(description)
    if desc_score is None:
        return score, done, critique
    guarded_score, counts = desc_score
    ...
    adjusted = score is None or score > guarded_score or bool(guard_notes)
    if adjusted:
        score = guarded_score
```

The guard replaces the verdict score with the description score if the verdict score is higher. This is meant to prevent the verdict pass from scoring higher than the description supports. However, if the description pass is too conservative (e.g., marking elements as PARTIAL when they are actually PRESENT), the guard caps the score unfairly. The loop may terminate early with a subpar artifact that the judge thinks is good enough.

---

## Recommended Fixes (Priority Order)

1. **Fix the model alias mismatch** — Remove `THELOOP_MODEL_CODER` from `.env` or change it to `Qwen3.6-Mesh-Code-Long`. This is the single highest-impact fix.
2. **Enable pi thinking** — Change `--pi-thinking=off` to `--pi-thinking=low` for SVG tasks. This lets the model plan before generating code.
3. **Shorten adapter notes** — Reduce `_ADAPTER_NOTES["svg"]` to 100-150 words. Move detailed guidance into the director prompt template.
4. **Increase pre-write tool budget** — Change `_LATER_ITER_PREWRITE_TOOL_LIMIT` to 12-15 for SVG tasks. This gives pi more slack to read and plan before writing.
5. **Increase no-write timeout** — Change `--pi-no-write-timeout-s` to 180-240 for SVG tasks. This gives pi more time to complete complex edits.
6. **Fix the leading space in `.env`** — Remove the leading space on line 5. This is a code style issue, not a bug.
7. **Improve the vision probe** — Retry with a larger image. Log a warning if the probe fails.

## Interaction Between Fixes

Fixes 1 and 2 are **synergistic**. Fix 1 gives pi the right model (Code-Long with 32K output tokens and 8K reasoning budget). Fix 2 lets the model use its reasoning budget to plan before generating code. Together, they should dramatically improve SVG quality.

Fixes 3, 4, and 5 are **defensive**. They reduce the chance of pi getting confused by verbose prompts or interrupted mid-fix. They are less impactful than fixes 1 and 2 but still worth implementing.

Fix 6 is **cosmetic**. It doesn't affect functionality but improves code readability.

Fix 7 is **diagnostic**. It helps detect vision probe failures early, which can cause the judge to miss visual defects.

---

## Verification Steps

1. **Check the model alias**: Run `python -m theloop.models` to see the current hat→alias mapping.
2. **Check the vision probe**: Run `python -m theloop.judge` to see if the vision probe passes.
3. **Check the pi thinking level**: Run `python -m theloop run examples/pelican.spec.md --log-level DEBUG` to see the pi thinking level in the logs.
4. **Check the pre-write tool budget**: Run `python -m theloop run examples/watch.spec.md --log-level DEBUG` to see if pi hits the pre-write limit.
5. **Check the no-write timeout**: Run `python -m theloop run examples/watch.spec.md --log-level DEBUG` to see if pi hits the no-write timeout.

---

*End of SVG regression analysis.*
