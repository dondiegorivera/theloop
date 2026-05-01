from theloop.judge import JudgeVerdict
from theloop.terminator import StopReason, TerminationConfig, Terminator


def _v(score: float | None, done: bool = False) -> JudgeVerdict:
    return JudgeVerdict(score=score, critique="", done=done, raw="")


def test_done_below_threshold_does_not_stop() -> None:
    terminator = Terminator(
        TerminationConfig(max_iters=10, score_threshold=0.99, no_improvement_for=5)
    )

    assert terminator.should_stop([_v(0.95, done=True)]) is None


def test_score_at_threshold_stops_even_if_done_false() -> None:
    terminator = Terminator(
        TerminationConfig(max_iters=10, score_threshold=0.99, no_improvement_for=5)
    )

    assert terminator.should_stop([_v(0.99, done=False)]) == StopReason.THRESHOLD


def test_done_at_threshold_reports_threshold() -> None:
    terminator = Terminator(
        TerminationConfig(max_iters=10, score_threshold=0.95, no_improvement_for=5)
    )

    assert terminator.should_stop([_v(0.95, done=True)]) == StopReason.THRESHOLD
