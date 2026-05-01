"""Composite stop condition over the judge verdict history.

Pure function — no I/O, no LLM calls — so the loop can ask "should I stop?"
after every iteration without ceremony.

Reasons (priority order, first match wins):

- `threshold`    — latest score >= `score_threshold`
- `done`         — the judge said it explicitly and the latest numeric score
                   is not below `score_threshold`
- `plateau`      — the best score over the most recent
                   `no_improvement_for` iterations did not strictly improve
                   over the best score seen before that window
- `max_iters`    — `len(history) >= max_iters`

`score_threshold` is the user's configured quality target. A judge `done=true`
below that threshold is treated as an optimistic judge signal, not a stop.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from theloop.judge import JudgeVerdict


class StopReason(StrEnum):
    DONE = "done"
    THRESHOLD = "threshold"
    PLATEAU = "plateau"
    MAX_ITERS = "max_iters"


@dataclass(frozen=True, slots=True)
class TerminationConfig:
    max_iters: int = 10
    score_threshold: float = 0.85
    no_improvement_for: int = 3


class Terminator:
    def __init__(self, config: TerminationConfig | None = None) -> None:
        self.config = config or TerminationConfig()

    def should_stop(self, history: list[JudgeVerdict]) -> StopReason | None:
        if not history:
            return None

        cfg = self.config
        latest = history[-1]

        if latest.score is not None and latest.score >= cfg.score_threshold:
            return StopReason.THRESHOLD
        if latest.done and (
            latest.score is None or latest.score >= cfg.score_threshold
        ):
            return StopReason.DONE

        # Plateau check: only meaningful once we have enough history to
        # compare a "recent window" against everything before it.
        n = cfg.no_improvement_for
        if n > 0 and len(history) > n:
            recent = history[-n:]
            prior = history[:-n]
            best_recent = _best(recent)
            best_prior = _best(prior)
            # If we have no scored verdict in either bucket, fall through.
            if best_recent is not None and best_prior is not None:
                if best_recent <= best_prior:
                    return StopReason.PLATEAU

        if len(history) >= cfg.max_iters:
            return StopReason.MAX_ITERS
        return None


def _best(verdicts: list[JudgeVerdict]) -> float | None:
    scores = [v.score for v in verdicts if v.score is not None]
    return max(scores) if scores else None


# ── manual smoke test ───────────────────────────────────────────────────────


def _v(score: float | None, done: bool = False) -> JudgeVerdict:
    return JudgeVerdict(score=score, critique="", done=done, raw="")


def _smoke() -> None:
    """Usage: python -m theloop.terminator"""
    cfg = TerminationConfig(max_iters=5, score_threshold=0.85, no_improvement_for=2)
    t = Terminator(cfg)

    cases: list[tuple[list[JudgeVerdict], StopReason | None]] = [
        ([], None),
        ([_v(0.3)], None),
        ([_v(0.3), _v(0.5)], None),
        ([_v(0.5, done=True)], None),
        ([_v(0.9, done=True)], StopReason.THRESHOLD),
        ([_v(0.9)], StopReason.THRESHOLD),
        ([_v(0.5), _v(0.6), _v(0.55), _v(0.55)], StopReason.PLATEAU),
        ([_v(0.5), _v(0.55), _v(0.6), _v(0.65)], None),  # still improving
        ([_v(0.3)] * 5, StopReason.PLATEAU),  # plateau triggers before max_iters
        ([_v(0.2), _v(0.3), _v(0.4), _v(0.5), _v(0.6)], StopReason.MAX_ITERS),
        ([_v(None), _v(None)], None),  # parse failures don't trigger plateau
    ]

    for hist, expected in cases:
        got = t.should_stop(hist)
        scores = [v.score for v in hist]
        ok = got == expected
        mark = "✓" if ok else "✗"
        print(f"{mark} scores={scores!r:50s} → {got}  (expected {expected})")
        assert ok

    print("\n✓ all assertions passed")


if __name__ == "__main__":
    _smoke()
