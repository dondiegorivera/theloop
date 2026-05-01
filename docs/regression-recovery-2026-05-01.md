# Regression Recovery Notes - 2026-05-01

This document summarizes the regression work done after the loop stopped
making meaningful improvements on visual SVG tasks, especially the watch and
robot runs.

## Context

The system is a closed improvement loop:

1. Planner updates the spec and chooses the next intent.
2. Director turns the intent into a Pi prompt.
3. Pi edits the workspace.
4. Adapter checks and renders the artifact.
5. Judge evaluates the rendered result.
6. Terminator decides whether to stop.

The regressions were visible in runs such as:

- `runs/20260429-200907-watch-spec`
- `runs/20260429-215010-watch-spec`
- `runs/20260430-194658-watch-spec`
- `runs/20260430-211804-watch-spec`
- `runs/20260430-225124-watch-spec`
- `runs/20260430-230458-watch-spec`
- `runs/20260501-084900-robot`
- `runs/20260501-091723-robot`

Earlier runs such as `runs/20260429-140421-watch-spec` showed the intended
behavior: the system rendered each changed iteration and made visible
artifact improvements.

## Problems Found

### Pi communication and path handling

Pi sometimes wrote helper files outside the workspace, for example
`/tmp/gen_watch.py`. Those writes did not appear in the run workspace, so the
loop could not render or judge the intended changes.

Pi also hallucinated stale absolute workspace paths, such as paths missing the
run suffix. That caused failed bash commands and contributed to read-only
turns.

### Large SVG output truncation

Detailed SVGs are often larger than the available single tool-output budget.
The model repeatedly tried to write a full `artifact.svg`, noticed truncation,
then retried the same large write or switched to unrelated helper scripts. Some
generated SVGs were around 37 KB / 17k tokens, which is too large for reliable
one-shot writes.

### Slow read-only Pi turns

Later iterations repeatedly spent minutes reading and reasoning about
`generate_artifact.py` without making an edit. In `runs/20260501-091723-robot`,
Pi found the relevant table/leg/chair sections, then performed an unbounded
`read generate_artifact.py` and burned the rest of the turn. This led to retry
loops, no workspace changes, and no new renders.

### Planner mutated the task

In `runs/20260501-084900-robot`, the source spec had a contradictory title and
body. The judge correctly identified that the named subject in the title was
missing, but the planner attempted to update the spec body to match the desired
pelican scene instead of treating the artifact as wrong. This let the planner
rewrite the user-authored contract instead of improving the artifact.

### Judge missed structural regressions

The judge sometimes scored local detail improvements while missing a major
whole-object regression. In the watch runs, gears were moved outside the clock
case, which should have been treated as a severe failure for a mechanical
watch. The judge needed stronger whole-subject and spatial sanity checks.

### No render after no-op iterations

When Pi made no workspace changes, the loop skipped render and reused the
previous verdict. This is intentional to avoid stochastic re-judging of the
same artifact, but it made failures look like render regressions. The actual
failure in those cases was upstream: Pi did not edit files.

## Fixes Applied

### Generator-first SVG workflow

SVG scaffolding now includes `generate_artifact.py`. The SVG adapter and
director guidance tell Pi to edit the generator and run:

```bash
python generate_artifact.py
```

For detailed or repetitive SVGs, Pi should not perform giant one-shot
`artifact.svg` writes.

### Absolute path protections

Pi guidance now requires relative paths for `read`, `write`, `edit`, `create`,
and bash commands. Prompts explicitly say that Pi already runs in the workspace
root and should not `cd` to `/src/...`.

`PiClient` detects absolute writes outside the workspace and logs a loud error.
`Workspace.reconcile_external_writes()` can recover external writes when the
file exists and can be mapped back into the workspace.

### No-write timeout and retry

The loop now supports `--pi-no-write-timeout-s`, defaulting to `120.0`. If Pi
does not call `write`, `edit`, or `create` within that window, the loop cancels
the turn and retries once with a shorter corrective prompt.

Retry prompts now tell Pi to make a concrete edit immediately, use relative
paths, avoid full generated reads, avoid package installs, regenerate, run one
targeted validation, then stop.

### Pre-write tool budget

Later iterations now have a hard pre-write policy:

- Iteration 0 is allowed to spend time generating the initial artifact.
- Later first attempts may use only a bounded number of tools before the first
  `write` / `edit` / `create`.
- Retry attempts are stricter.
- An unbounded pre-write `read generate_artifact.py` is treated as an immediate
  failed attempt.

This is meant to stop multi-minute read-only loops and force failures to happen
quickly.

### Compact Pi live logs

Each Pi attempt now writes a compact live trace under:

```text
runs/<run-id>/artifacts/iter-N/pi_live.log
runs/<run-id>/artifacts/iter-N/pi_live_retry1.log
```

The trace records turn boundaries, tool calls, and short text/thinking samples
instead of dumping full token streams.

### Planner spec preservation

The planner may append an `## Iteration history` section, but it can no longer
rewrite the user-authored spec body. If the planner returns a condensed,
bloated, SVG-injected, or rewritten spec, the loop preserves the prior spec.

If the planner intent says to update or rewrite the spec, the loop retargets
that intent into artifact work. For example, a planner response like "update
the spec body" becomes "revise the artifact so it visibly depicts the primary
heading".

### Director authoritative spec

The director now receives the full authoritative spec in addition to the
planner intent and workspace inventory. The final Pi prompt includes the spec
as the source of truth, so a narrow or ambiguous iteration directive cannot
drop required elements.

### Judge improvements

The judge now performs a two-pass evaluation:

1. Describe/classify required elements as `PRESENT`, `PARTIAL`, `HIDDEN`, or
   `MISSING`.
2. Score from that evidence.

Additional guards were added for:

- Named subject missing.
- Position-specific contradictions, such as watch hands requested at 10 and 2
  but described around 12.
- Whole-subject sanity checks.
- Mechanical watch movement/gears outside the case.

The spatial guard can cap severe watch layout failures around `0.65`.

### Rendering and reports

Visual rendering resolution was increased to `1536x1152`. Reports now include
the root source spec, making it easier to distinguish the user-authored spec
from planner-evolved iteration specs.

## Tests Added or Expanded

Tests now cover:

- Judge scoring and deterministic guard behavior.
- Planner rejection of condensed specs.
- Planner rejection of bloated specs.
- Planner rejection of generated SVG injected into a spec.
- Planner rejection of rewritten user-authored spec bodies.
- Retry prompt constraints.
- Pre-write policy behavior.
- Workspace reconciliation of external writes.

As of this checkpoint:

```text
.venv/bin/python -m pytest
25 passed

.venv/bin/python -m compileall src/theloop
clean
```

## Current Behavior to Expect

If Pi edits files, the loop should run the adapter check, render, judge, and
commit normally.

If Pi makes no workspace changes, later iterations will skip render and reuse
the previous verdict. This means "no render after iter 0" usually means "Pi did
not edit anything", not that the renderer itself failed.

If Pi spends too long inspecting before editing, the new pre-write guard should
fail the attempt earlier and retry with a stricter prompt. If retry also fails,
the iteration will be recorded as a no-op.

## Remaining Risks

The system still depends on Pi following prompts. Runtime guards now bound the
worst read-only loops, but they cannot guarantee a good edit.

The generator-first SVG workflow improves reliability for visual tasks, but it
may not be appropriate for every adapter or generic task. The path and no-write
guards were written to be generic, while SVG-specific guidance remains scoped
to the SVG adapter notes.

The judge is stronger, but visual judgment remains probabilistic. The added
deterministic guards cover known failure classes; new task domains may need
new domain-specific sanity checks.

## Practical Debug Checklist

For a bad run, inspect in this order:

1. `events.jsonl`: check whether Pi called `write`, `edit`, or `create`.
2. `artifacts/iter-N/pi_live.log`: check whether Pi got stuck reading or
   thinking.
3. `artifacts/iter-N/pi_prompt.txt`: check whether the directive still asks
   for too much inspection.
4. `git -C runs/<run>/workspace log --stat`: confirm whether commits contain
   real file changes or empty/no-op iterations.
5. `artifacts/iter-N/render.png`: if missing, check whether there were
   workspace changes before blaming render.
6. `artifacts/iter-N/judge_description.txt`: compare the judge evidence to the
   rendered image when score/regression looks wrong.
