"""Judge — two-pass LiteLLM evaluation → JSON verdict.

Pass 1 (`_describe`) produces a literal description of the artifact: object
enumeration for images, structural enumeration for text. The describe call
sees the spec only as context for what to look for, never as something to
score against. Vision path uses JUDGE_VISION; text path uses JUDGE_TEXT.

Pass 2 (`evaluate`) reads spec + first-pass description + last coder output
and returns the JSON verdict. Always JUDGE_TEXT — by the time the verdict
pass runs, all the visual extraction has already happened. The raw artifact is
not sent to pass 2; otherwise the model can re-examine it and contradict the
description it is supposed to score from.

Why two passes: a single-call judge collapses observation and judgment,
which lets the model rubber-stamp obviously-broken artifacts ("a pelican
riding a bike", scoring 1.0 even when the bike has no frame). Forcing the
model to commit to a description first makes structural defects survive
into the scoring pass.

A startup `vision_probe()` checks whether the configured JUDGE_VISION
alias actually returns image-aware output; on failure the describe pass
falls back to text-only.
"""

from __future__ import annotations

import base64
import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path

from openai import AsyncOpenAI

from theloop.models import Hat, LiteLLMConfig, alias_for, litellm_config

log = logging.getLogger(__name__)

_PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
_FENCE_RE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$", re.MULTILINE)

# Soft cap on how much we feed the first-pass model for description, to
# keep the describe call bounded. Doc artifacts can be 25KB+; vision pass
# doesn't see this anyway, and for text the verdict pass sees the full
# artifact regardless.
_DESCRIBE_TEXT_LIMIT = 12_000
_CLASSIFICATION_CREDIT = {
    "PRESENT": 1.0,
    "HIDDEN": 0.5,
    "PARTIAL": 0.4,
    "MISSING": 0.0,
}
_CLASSIFICATION_RE = re.compile(r"\b(PRESENT|PARTIAL|HIDDEN|MISSING)\b")

# 32×32 solid-red PNG. llama.cpp's vision encoder rejects very small images,
# so the probe needs something the vision tokenizer can actually process.
# We use red specifically so the sentinel ("RED") is unambiguous.
_PROBE_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAKElEQVR4nO3NsQ0AAAzCMP5/"
    "un0CNkuZ41wybXsHAAAAAAAAAAAAxR4yw/wuPL6QkAAAAABJRU5ErkJggg=="
)
_PROBE_PROMPT = (
    "What is the dominant color of this image? Reply with exactly one word: "
    "the color name, lowercase, no punctuation."
)
_PROBE_SENTINEL = "red"


@dataclass(frozen=True, slots=True)
class JudgeVerdict:
    score: float | None  # None on parse failure
    critique: str
    done: bool
    raw: str  # original model output, kept for debugging
    description: str = ""  # first-pass concrete description (empty pre-two-pass)
    hard_failures: list[str] | None = None
    dimensions: dict[str, float] | None = None
    next_action: str = ""
    regression_against_best: bool = False


class Judge:
    def __init__(
        self,
        config: LiteLLMConfig | None = None,
        *,
        prompt_template: str | None = None,
        describe_template: str | None = None,
        prose_prompt_template: str | None = None,
        prose_describe_template: str | None = None,
        vision_available: bool | None = None,
    ) -> None:
        self.config = config or litellm_config()
        self.prompt_template = prompt_template or (_PROMPTS_DIR / "judge.md").read_text()
        self.describe_template = describe_template or (_PROMPTS_DIR / "judge_describe.md").read_text()
        self.prose_prompt_template = (
            prose_prompt_template or (_PROMPTS_DIR / "judge_prose.md").read_text()
        )
        self.prose_describe_template = (
            prose_describe_template
            or (_PROMPTS_DIR / "judge_describe_prose.md").read_text()
        )
        # None = unknown (probe not yet run); True/False = decided.
        self.vision_available: bool | None = vision_available
        self._client = AsyncOpenAI(base_url=self.config.base_url, api_key=self.config.api_key)

    # ── vision probe ──────────────────────────────────────────────────────

    async def vision_probe(self) -> bool:
        """Decide whether the loaded backbone can actually see images.

        Sets and returns `self.vision_available`. The openai client already
        retries 500-class errors twice; we add one more retry on 503/loading
        in case llama.cpp is mid-load. Anything else (including a 500 that
        survives openai's retries — i.e. the model genuinely cannot process
        images) means no vision, and we fall back fast.
        """
        import asyncio

        alias = alias_for(Hat.JUDGE_VISION)
        for attempt in range(2):
            try:
                resp = await self._client.chat.completions.create(
                    model=alias,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": _PROBE_PROMPT},
                                {
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/png;base64,{_PROBE_PNG_B64}"},
                                },
                            ],
                        }
                    ],
                    max_tokens=16,
                    temperature=0.0,
                )
                reply = (resp.choices[0].message.content or "").strip()
                break
            except Exception as e:
                msg = str(e)
                loading = "503" in msg or "Loading model" in msg
                if loading and attempt == 0:
                    log.info("vision probe: model loading, retrying once in 5s...")
                    await asyncio.sleep(5.0)
                    continue
                log.warning("vision probe failed (%s); falling back to text-only judge", e)
                self.vision_available = False
                return False

        ok = _PROBE_SENTINEL in reply.lower()
        if not ok:
            log.warning(
                "vision probe returned %r — model does not appear to see images; "
                "falling back to text-only judge",
                reply,
            )
        else:
            log.info("vision probe ok (model saw the red square: %r)", reply)
        self.vision_available = ok
        return ok

    # ── evaluation ────────────────────────────────────────────────────────

    async def evaluate(
        self,
        spec: str,
        png_path: Path | None,
        last_pi_output: str,
        artifact_text: str | None = None,
        score_threshold: float | None = None,
        judge_profile: str = "text_presence",
    ) -> JudgeVerdict:
        """Two-pass judge: describe → score.

        Pass 1 produces a concrete description of the artifact (vision call
        if a render is available, text otherwise). Pass 2 reads spec +
        description and returns the JSON verdict. The structural separation
        forces the model to commit to observations before scoring.
        """
        use_vision = bool(png_path) and self.vision_available is not False

        # ── Pass 1: describe ─────────────────────────────────────────────
        description = await self._describe(
            png_path=png_path if use_vision else None,
            artifact_text=artifact_text,
            spec=spec,
            judge_profile=judge_profile,
        )

        # ── Pass 2: score ────────────────────────────────────────────────
        # Deliberately *do not* pass the raw artifact (image or source) to
        # the verdict pass. The describe pass already examined the artifact
        # and committed to PRESENT/PARTIAL/HIDDEN/MISSING with evidence.
        # Letting verdict re-examine has been observed to override the
        # describe pass on negative findings ("balance wheel MISSING" → "is
        # correctly positioned"), which destroys the whole two-stage design.
        verdict_alias = alias_for(Hat.JUDGE_TEXT)

        verdict_template = (
            self.prose_prompt_template
            if judge_profile == "prose_quality"
            else self.prompt_template
        )
        verdict_text = (
            f"{verdict_template}\n\n"
            "## Spec\n"
            f"{spec.strip()}\n\n"
            "## First-pass description\n"
            f"{description.strip()}\n\n"
            "## Last coder output\n"
            f"{(last_pi_output or '(empty)').strip()}\n"
        )

        resp = await self._client.chat.completions.create(
            model=verdict_alias,
            messages=[{"role": "user", "content": verdict_text}],
            temperature=0.0,
        )
        raw = (resp.choices[0].message.content or "").strip()
        return _parse_verdict(
            raw,
            description=description,
            spec=spec,
            score_threshold=score_threshold,
            judge_profile=judge_profile,
        )

    async def _describe(
        self,
        png_path: Path | None,
        artifact_text: str | None,
        spec: str,
        judge_profile: str = "text_presence",
    ) -> str:
        """First pass: concrete description of the artifact, no scoring."""
        if png_path is not None:
            alias = alias_for(Hat.JUDGE_VISION)
            artifact_block = "(see attached image)"
        else:
            alias = alias_for(Hat.JUDGE_TEXT)
            if artifact_text:
                trimmed = artifact_text.strip()
                if len(trimmed) > _DESCRIBE_TEXT_LIMIT:
                    trimmed = (
                        trimmed[:_DESCRIBE_TEXT_LIMIT]
                        + f"\n\n... (truncated; full artifact is {len(artifact_text)} chars)"
                    )
                artifact_block = trimmed
            else:
                artifact_block = "(no artifact provided)"

        # The describe pass sees the spec only as context for *what to look
        # for* (e.g. a bicycle has these parts), not as something to score
        # against. The prompt explicitly forbids evaluation.
        describe_template = (
            self.prose_describe_template
            if judge_profile == "prose_quality"
            else self.describe_template
        )
        user_text = (
            f"{describe_template}\n\n"
            "## Spec (for context only — do not evaluate against it)\n"
            f"{spec.strip()}\n\n"
            "## Artifact\n"
            f"{artifact_block}"
        )

        content: list[dict] = [{"type": "text", "text": user_text}]
        if png_path is not None:
            b64 = base64.b64encode(png_path.read_bytes()).decode("ascii")
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64}"},
                }
            )

        try:
            resp = await self._client.chat.completions.create(
                model=alias,
                messages=[{"role": "user", "content": content}],
                temperature=0.0,
            )
            return (resp.choices[0].message.content or "").strip()
        except Exception as e:
            log.warning("describe pass failed (%s); verdict pass will run without it", e)
            return f"(describe pass failed: {e})"


def _parse_verdict(
    raw: str,
    *,
    description: str = "",
    spec: str = "",
    score_threshold: float | None = None,
    judge_profile: str = "text_presence",
) -> JudgeVerdict:
    body = _FENCE_RE.sub("", raw).strip()
    try:
        obj = json.loads(body)
        score = obj.get("score")
        score_f = float(score) if score is not None else None
        hard_failures = _coerce_string_list(obj.get("hard_failures"))
        dimensions = _coerce_dimension_scores(obj.get("dimensions"))
        next_action = str(obj.get("next_action") or "").strip()
        regression = bool(obj.get("regression_against_best", False))
        score_f, done, critique = _apply_description_score_guard(
            score=score_f,
            done=bool(obj.get("done", False)),
            critique=str(obj.get("critique", "")).strip(),
            description=description,
            spec=spec,
        )
        if judge_profile == "prose_quality" and hard_failures:
            done = False
        score_f, done, critique = _apply_threshold_actionability_guard(
            score=score_f,
            done=done,
            critique=critique,
            description=description,
            score_threshold=score_threshold,
        )
        return JudgeVerdict(
            score=score_f,
            critique=critique,
            done=done,
            raw=raw,
            description=description,
            hard_failures=hard_failures,
            dimensions=dimensions,
            next_action=next_action,
            regression_against_best=regression,
        )
    except (json.JSONDecodeError, TypeError, ValueError) as e:
        log.warning("judge output did not parse as JSON (%s); raw=%r", e, raw[:200])
        return JudgeVerdict(
            score=None, critique=raw[:500], done=False, raw=raw, description=description
        )


def _coerce_string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def _coerce_dimension_scores(value: object) -> dict[str, float]:
    if not isinstance(value, dict):
        return {}
    scores: dict[str, float] = {}
    for key, raw_score in value.items():
        try:
            score = float(raw_score)
        except (TypeError, ValueError):
            continue
        scores[str(key)] = max(0.0, min(1.0, score))
    return scores


def _apply_description_score_guard(
    *,
    score: float | None,
    done: bool,
    critique: str,
    description: str,
    spec: str = "",
) -> tuple[float | None, bool, str]:
    """Keep verdict scoring bounded by first-pass classifications.

    Prompt instructions alone are not enough here: the regression that
    triggered this guard was a verdict pass scoring 0.95 while its own
    first-pass description marked multiple required elements MISSING/PARTIAL.
    The parser is intentionally conservative and only acts when the
    description contains explicit uppercase classifications.
    """
    desc_score = _score_from_description(description)
    if desc_score is None:
        return score, done, critique

    guarded_score, counts = desc_score
    contradiction_note = _apply_position_contradiction_guard(
        counts=counts,
        description=description,
        spec=spec,
    )
    layout_note = _apply_spatial_layout_guard(
        counts=counts,
        description=description,
        spec=spec,
    )
    guard_notes = [note for note in (contradiction_note, layout_note) if note]
    if guard_notes:
        guarded_score = _score_from_counts(counts)
    if layout_note:
        guarded_score = min(guarded_score, 0.65)
    defects = counts["HIDDEN"] + counts["PARTIAL"] + counts["MISSING"]
    adjusted = score is None or score > guarded_score or bool(guard_notes)
    if adjusted:
        score = guarded_score
        suffix = (
            " Score adjusted from first-pass classifications: "
            f"{counts['PRESENT']} PRESENT, {counts['HIDDEN']} HIDDEN, "
            f"{counts['PARTIAL']} PARTIAL, {counts['MISSING']} MISSING."
        )
        if guard_notes:
            suffix += " " + " ".join(guard_notes)
        critique = (critique + suffix).strip() if critique else suffix.strip()

    if score is None or score < 0.95 or defects:
        done = False
    return score, done, critique


_NO_DEFECT_RE = re.compile(
    r"\b("
    r"no (?:visible |significant |major )?(?:defects?|issues?|problems?)"
    r"|all required elements (?:are )?present"
    r"|meets all (?:spec )?requirements"
    r"|successfully (?:includes|satisfies)"
    r")\b",
    re.IGNORECASE,
)


def _apply_threshold_actionability_guard(
    *,
    score: float | None,
    done: bool,
    critique: str,
    description: str,
    score_threshold: float | None,
) -> tuple[float | None, bool, str]:
    """A below-threshold verdict must give the planner a real next defect."""
    if score_threshold is None or score is None or score >= score_threshold:
        return score, done, critique

    done = False
    if not _NO_DEFECT_RE.search(critique or ""):
        return score, done, critique

    improvement = _visible_improvement_hint(description)
    note = (
        f"Score {score:.2f} is below the configured threshold "
        f"{score_threshold:.2f}, so the artifact is not done. "
        f"{improvement}"
    )
    return score, done, note


def _visible_improvement_hint(description: str) -> str:
    desc_l = description.lower()
    if any(word in desc_l for word in ("newspaper", "text", "headline", "label")):
        return (
            "Inspect and fix the most visible remaining layout issue, especially "
            "text containment, clipping, overlap, or newspaper legibility."
        )
    return (
        "Inspect and fix the most visible remaining issue in composition, "
        "legibility, alignment, spatial coherence, or action clarity."
    )


def _score_from_description(description: str) -> tuple[float, dict[str, int]] | None:
    counts = {key: 0 for key in _CLASSIFICATION_CREDIT}
    for line in description.splitlines():
        matches = _CLASSIFICATION_RE.findall(line)
        # Skip legends/summaries like "PRESENT / PARTIAL / HIDDEN / MISSING".
        if len(set(matches)) != 1:
            continue
        counts[matches[0]] += 1

    total = sum(counts.values())
    if total == 0:
        return None

    return _score_from_counts(counts), counts


def _score_from_counts(counts: dict[str, int]) -> float:
    total = sum(counts.values())
    if total == 0:
        return 0.05
    earned = sum(counts[k] * _CLASSIFICATION_CREDIT[k] for k in counts)
    return round(0.05 + 0.90 * (earned / total), 2)


def _apply_position_contradiction_guard(
    *,
    counts: dict[str, int],
    description: str,
    spec: str,
) -> str:
    """Downgrade obvious PRESENT classifications contradicted by evidence.

    The vision pass can say "Hour Hand: PRESENT — points directly upwards"
    even when the spec requires the hour hand near 10 o'clock. The formula
    guard only sees classifications, so catch the narrow class of
    position-specific contradictions deterministically.
    """
    spec_l = spec.lower()
    if not spec_l:
        return ""

    downgraded: list[str] = []
    for line in description.splitlines():
        line_l = line.lower()
        if "present" not in line_l:
            continue
        if _requires_clock_position(spec_l, "hour", "10") and _line_is_hand_at_12(
            line_l, "hour"
        ):
            downgraded.append("hour hand")
        if _requires_clock_position(spec_l, "minute", "2") and _line_is_hand_at_12(
            line_l, "minute"
        ):
            downgraded.append("minute hand")

    unique = sorted(set(downgraded))
    if not unique:
        return ""
    shift = min(len(unique), counts.get("PRESENT", 0))
    counts["PRESENT"] -= shift
    counts["PARTIAL"] += shift
    return (
        "Position-specific contradiction guard downgraded "
        + ", ".join(unique)
        + " from PRESENT to PARTIAL because the description says the hand "
        "points to 12/XII while the spec requires a different clock position."
    )


def _apply_spatial_layout_guard(
    *,
    counts: dict[str, int],
    description: str,
    spec: str,
) -> str:
    """Penalize common-sense layout failures that break the subject.

    A watch with its gear train outside the case may still have "gears"
    and a "case" in a checklist sense, but it no longer reads as a plausible
    mechanical watch. Treat that as a missing movement integration rather
    than a minor partial.
    """
    spec_l = spec.lower()
    if "watch" not in spec_l or "movement" not in spec_l or "gear" not in spec_l:
        return ""
    bad_lines: list[str] = []
    for line in description.splitlines():
        line_l = line.lower()
        if "movement" not in line_l and "gear" not in line_l:
            continue
        if "outside" not in line_l:
            continue
        if "case" not in line_l and "watch" not in line_l and "boundary" not in line_l:
            continue
        if "partial" in line_l:
            bad_lines.append(line)

    if not bad_lines:
        return ""
    if counts.get("PARTIAL", 0) > 0:
        counts["PARTIAL"] -= 1
        counts["MISSING"] += 1
    return (
        "Spatial-layout guard downgraded the movement/gears from PARTIAL to "
        "MISSING because the description says they are outside the watch case, "
        "which breaks the mechanical watch structure."
    )


def _requires_clock_position(spec_l: str, hand: str, hour: str) -> bool:
    hand_idx = spec_l.find(f"{hand} hand")
    if hand_idx == -1:
        return False
    window = spec_l[hand_idx : hand_idx + 180]
    return (
        f"{hour} o'clock" in window
        or f"{hour} o’clock" in window
        or f"position {hour}" in window
        or f"near {hour}" in window
    )


def _line_is_hand_at_12(line_l: str, hand: str) -> bool:
    if f"{hand} hand" not in line_l:
        return False
    return (
        "directly upwards" in line_l
        or "straight up" in line_l
        or "towards xii" in line_l
        or "toward xii" in line_l
        or "towards 12" in line_l
        or "toward 12" in line_l
        or "12:00" in line_l
    )


# ── manual smoke test ───────────────────────────────────────────────────────

async def _smoke() -> None:
    """Usage: python -m theloop.judge

    Runs vision probe against the live LiteLLM proxy, then does a real
    evaluate() call. Re-uses the SVG adapter to produce a render PNG.
    """
    import tempfile

    from theloop.adapters.svg import SVGAdapter
    from theloop.renderer import Renderer
    from theloop.workspace import Workspace

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    judge = Judge()
    print(f"alias (vision): {alias_for(Hat.JUDGE_VISION)}")
    print(f"alias (text):   {alias_for(Hat.JUDGE_TEXT)}")
    print("running vision probe...")
    has_vision = await judge.vision_probe()
    print(f"  vision_available = {has_vision}")

    with tempfile.TemporaryDirectory(prefix="theloop-judge-") as tmp:
        ws = Workspace.create(Path(tmp), slug="judge-smoke")
        adapter = SVGAdapter()
        ws.begin_iteration(0)
        adapter.prepare(ws.workspace_path)
        out_png = ws.artifact_dir(0) / "render.png"
        async with Renderer() as r:
            await adapter.render(ws.workspace_path, out_png, r)

        spec = (
            "Draw an SVG of a pelican riding a bicycle. The pelican should be "
            "recognizable. Bike has two wheels and a frame."
        )
        print("calling judge.evaluate() on the placeholder render...")
        verdict = await judge.evaluate(
            spec=spec,
            png_path=out_png if has_vision else None,
            last_pi_output="(initial scaffold; no edits yet)",
        )
        print(f"  score:    {verdict.score}")
        print(f"  done:     {verdict.done}")
        print(f"  critique: {verdict.critique[:240]}")
        if verdict.score is None:
            print(f"  RAW: {verdict.raw[:240]}")

        # On a placeholder gray rect for a pelican spec, we'd expect a low
        # score — assert only that we got *some* parseable output.
        assert verdict.raw, "judge returned empty output"
        print("✓ judge round-trip ok")


if __name__ == "__main__":
    import asyncio

    asyncio.run(_smoke())
