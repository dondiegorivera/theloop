from theloop.judge import _parse_verdict, _score_from_description


def test_description_score_matches_watch_regression_math() -> None:
    lines = [f"- present item {i}: PRESENT - visible" for i in range(22)]
    lines += [f"- partial item {i}: PARTIAL - incomplete" for i in range(3)]
    lines += [f"- missing item {i}: MISSING - absent" for i in range(3)]

    score, counts = _score_from_description("\n".join(lines)) or (None, {})

    assert counts == {"PRESENT": 22, "HIDDEN": 0, "PARTIAL": 3, "MISSING": 3}
    assert score == 0.8


def test_verdict_score_is_capped_by_first_pass_description() -> None:
    description = "\n".join(
        [
            "- Main watch case: PRESENT - visible.",
            "- Crown: PRESENT - visible.",
            "- Balance wheel in bottom-right quadrant: MISSING - outside the case.",
            "- Gear train integration: PARTIAL - gears are disconnected.",
        ]
    )
    raw = '{"score": 0.95, "critique": "Looks correct.", "done": true}'

    verdict = _parse_verdict(raw, description=description)

    assert verdict.score == 0.59
    assert verdict.done is False
    assert "2 PRESENT" in verdict.critique
    assert "1 PARTIAL" in verdict.critique
    assert "1 MISSING" in verdict.critique


def test_verdict_lower_than_description_score_is_preserved() -> None:
    description = "\n".join(
        [
            "- Main subject: PRESENT - visible.",
            "- Required detail: PRESENT - visible.",
        ]
    )
    raw = '{"score": 0.7, "critique": "Still rough.", "done": false}'

    verdict = _parse_verdict(raw, description=description)

    assert verdict.score == 0.7
    assert verdict.done is False
    assert verdict.critique == "Still rough."


def test_position_specific_hand_contradiction_blocks_done() -> None:
    spec = (
        "Draw a watch with an hour hand pointing near the 10 o'clock position "
        "and a minute hand pointing near the 2 o'clock position."
    )
    description = "\n".join(
        [
            "- Watch: PRESENT - visible.",
            "- Hour Hand: PRESENT - a black hand points directly upwards towards XII.",
            "- Minute Hand: PRESENT - a black hand points directly upwards towards XII.",
            "- Second Hand: PRESENT - a red line points near 7 o'clock.",
        ]
    )
    raw = '{"score": 0.95, "critique": "Looks correct.", "done": true}'

    verdict = _parse_verdict(raw, description=description, spec=spec)

    assert verdict.score == 0.68
    assert verdict.done is False
    assert "Position-specific contradiction guard" in verdict.critique


def test_spatial_layout_guard_penalizes_gears_outside_watch_case() -> None:
    spec = (
        "Draw a mechanical pocket watch with movement gears visible through "
        "a caseback or cutaway in the bottom half of the watch."
    )
    description = "\n".join(
        [
            "- Case & Crown: PRESENT — circular case and crown are visible.",
            "- Dial: PRESENT — dial is visible.",
            "- Hands: PRESENT — hands are visible.",
            "- Movement: PARTIAL — gears are located outside and below the main case boundary rather than visible through a cutaway within the watch.",
            "- Chain: PRESENT — chain is visible.",
        ]
    )
    raw = '{"score": 0.95, "critique": "Looks correct.", "done": true}'

    verdict = _parse_verdict(raw, description=description, spec=spec)

    assert verdict.score == 0.65
    assert verdict.done is False
    assert "Spatial-layout guard" in verdict.critique


def test_below_threshold_no_defect_verdict_gets_actionable_critique() -> None:
    description = "\n".join(
        [
            "- Victorian-era robot: PRESENT — visible brass robot.",
            "- Reading a newspaper: PRESENT — open newspaper with headline and text.",
            "- In a cafe: PRESENT — table, cup, and window are visible.",
            "",
            "## Other observations",
            "The composition is centered.",
        ]
    )
    raw = (
        '{"score": 0.95, "critique": "All required elements are present and '
        'there are no visible defects.", "done": true}'
    )

    verdict = _parse_verdict(
        raw,
        description=description,
        score_threshold=0.99,
    )

    assert verdict.score == 0.95
    assert verdict.done is False
    assert "below the configured threshold 0.99" in verdict.critique
    assert "text containment" in verdict.critique
