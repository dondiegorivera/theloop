import json

from theloop.orchestrator import _compose_pi_prompt, _normalize_markdown, _parse_plan


def test_parse_plan_rejects_condensed_spec() -> None:
    fallback = (
        "---\n"
        "adapter: svg\n"
        "max_iters: 10\n"
        "---\n"
        "# Mechanical Pocket Watch\n\n"
        + "\n".join(f"- Required detail {i}: must remain explicit." for i in range(40))
    )
    raw = json.dumps(
        {
            "spec": "---\nadapter: svg\nmax_iters: 10\n---\n# Short watch spec\nDraw a watch.",
            "intent": "Draw the full watch.",
        }
    )

    plan = _parse_plan(raw, fallback_spec=fallback)

    assert plan.spec == _normalize_markdown(fallback)
    assert plan.intent == "Draw the full watch."


def test_parse_plan_accepts_preserved_spec_with_history() -> None:
    fallback = "---\nadapter: svg\n---\n# Spec\n\n" + "A detailed requirement. " * 60
    updated = fallback + "\n\n## Iteration history\n- iter 0: draw the subject."
    raw = json.dumps({"spec": updated, "intent": "Add the missing detail."})

    plan = _parse_plan(raw, fallback_spec=fallback)

    assert plan.spec == _normalize_markdown(updated)
    assert plan.intent == "Add the missing detail."


def test_parse_plan_uses_default_intent_when_missing() -> None:
    fallback = "---\nadapter: svg\n---\n# Spec\n\nDraw the required artifact."
    raw = json.dumps({"spec": fallback})

    plan = _parse_plan(raw, fallback_spec=fallback)

    assert plan.spec == _normalize_markdown(fallback)
    assert "Implement the spec" in plan.intent


def test_parse_plan_rejects_bloated_spec() -> None:
    fallback = "---\nadapter: svg\n---\n# Spec\n\nDraw the required artifact."
    bloated = fallback + "\n\n" + ("Extra rewritten detail. " * 200)
    raw = json.dumps({"spec": bloated, "intent": "Draw the artifact."})

    plan = _parse_plan(raw, fallback_spec=fallback)

    assert plan.spec == _normalize_markdown(fallback)
    assert plan.intent == "Draw the artifact."


def test_parse_plan_rejects_generated_svg_injected_into_spec() -> None:
    fallback = "---\nadapter: svg\n---\n# Spec\n\nDraw a watch with hands at 10 and 2."
    injected = fallback + "\n\n<svg><circle cx=\"0\" cy=\"0\" r=\"10\" /></svg>"
    raw = json.dumps({"spec": injected, "intent": "Draw the watch."})

    plan = _parse_plan(raw, fallback_spec=fallback)

    assert plan.spec == _normalize_markdown(fallback)
    assert "<svg" not in plan.spec
    assert plan.intent == "Draw the watch."


def test_parse_plan_rejects_rewritten_user_contract() -> None:
    fallback = (
        "---\n"
        "adapter: svg\n"
        "---\n"
        "# Pelican on a bicycle with city behind, postcard\n\n"
        "An svg image of a Victorian-era robot reading a newspaper in a cafe\n"
    )
    rewritten = (
        "---\n"
        "adapter: svg\n"
        "---\n"
        "# Pelican on a bicycle with city behind, postcard\n\n"
        "An svg image of a pelican riding a bicycle through a city postcard.\n"
    )
    raw = json.dumps(
        {
            "spec": rewritten,
            "intent": "Update the spec body to describe a pelican riding a bicycle instead of a Victorian robot.",
        }
    )

    plan = _parse_plan(raw, fallback_spec=fallback)

    assert plan.spec == _normalize_markdown(fallback)
    assert "visibly depicts Pelican on a bicycle" in plan.intent
    assert "Do not change the spec text" in plan.intent


def test_parse_plan_retargets_non_actionable_final_intent() -> None:
    fallback = (
        "---\n"
        "adapter: svg\n"
        "---\n"
        "# A Victorian-era robot reading a newspaper in a cafe\n\n"
        "An svg image of a Victorian-era robot reading a newspaper in a cafe\n"
    )
    raw = json.dumps(
        {
            "spec": fallback + "\n\n## Iteration history\n- iter 0: draw scene.",
            "intent": "The artifact successfully satisfies all specified requirements. This iteration should verify the final output against the 0.99 score threshold and conclude the generation process, as no further structural or aesthetic changes are necessary.",
        }
    )

    plan = _parse_plan(raw, fallback_spec=fallback)

    assert "Make one concrete visible improvement" in plan.intent
    assert "Do not merely verify" in plan.intent


def test_compose_pi_prompt_keeps_authoritative_spec_visible() -> None:
    prompt = _compose_pi_prompt(
        spec="# Watch\n\n- Roman numerals I through XII\n- Crown chain",
        directive="Add missing polish.",
    )

    assert prompt.index("## Authoritative spec") < prompt.index("## Iteration directive")
    assert "Roman numerals I through XII" in prompt
    assert "Crown chain" in prompt
    assert "Add missing polish." in prompt
    assert "Call `write` or `edit`" in prompt
    assert "Use relative paths only" in prompt
