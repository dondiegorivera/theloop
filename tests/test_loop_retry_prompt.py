from theloop.judge import JudgeVerdict
from theloop.loop import (
    _compose_pi_retry_prompt,
    _critique_for_next_plan,
    _prewrite_policy_violation,
)


def test_retry_prompt_is_short_and_forbids_full_generated_reads() -> None:
    original = (
        "## Authoritative spec\n"
        + ("Draw a detailed watch. " * 400)
        + "\n\n## Iteration directive\n"
        "Fix the small seconds sub-dial.\n\n"
        "## Execution rule\n"
        "Call edit promptly."
    )

    retry = _compose_pi_retry_prompt(original)

    assert len(retry) < len(original)
    assert "Fix the small seconds sub-dial" in retry
    assert "Do not read full `artifact.svg`" in retry
    assert "At most one locating" in retry
    assert "Do not read the full generator" in retry
    assert "Use relative paths only" in retry
    assert "Do not install packages" in retry
    assert "spec truncated for retry" in retry


def test_prewrite_policy_allows_iter0_long_generation() -> None:
    assert (
        _prewrite_policy_violation(
            it=0,
            attempt=0,
            tool="read",
            args={"path": "generate_artifact.py"},
            tool_count=20,
        )
        is None
    )


def test_prewrite_policy_blocks_later_unbounded_generator_read() -> None:
    reason = _prewrite_policy_violation(
        it=2,
        attempt=0,
        tool="read",
        args={"path": "generate_artifact.py"},
        tool_count=1,
    )

    assert reason is not None
    assert "unbounded read" in reason


def test_prewrite_policy_allows_small_scaffold_generator_read(tmp_path) -> None:
    generator = tmp_path / "generate_artifact.py"
    generator.write_text("print('small scaffold')\n")

    assert (
        _prewrite_policy_violation(
            it=2,
            attempt=0,
            tool="read",
            args={"path": "generate_artifact.py"},
            tool_count=1,
            workspace=tmp_path,
        )
        is None
    )


def test_prewrite_policy_blocks_retry_tool_loops() -> None:
    reason = _prewrite_policy_violation(
        it=2,
        attempt=1,
        tool="bash",
        args={"command": "grep -n table generate_artifact.py"},
        tool_count=5,
    )

    assert reason is not None
    assert "without calling write/edit/create" in reason


def test_done_below_threshold_gets_concrete_next_plan_note() -> None:
    critique = _critique_for_next_plan(
        JudgeVerdict(
            score=0.95,
            critique="All required elements are present.",
            done=True,
            raw="",
        ),
        score_threshold=0.99,
    )

    assert critique is not None
    assert "below the configured threshold 0.99" in critique
    assert "Do not verify" in critique
    assert "one concrete visible artifact improvement" in critique
