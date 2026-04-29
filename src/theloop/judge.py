"""Judge — two-pass LiteLLM evaluation → JSON verdict.

Pass 1 (`_describe`) produces a literal description of the artifact: object
enumeration for images, structural enumeration for text. The describe call
sees the spec only as context for what to look for, never as something to
score against. Vision path uses JUDGE_VISION; text path uses JUDGE_TEXT.

Pass 2 (`evaluate`) reads spec + first-pass description + artifact text +
last coder output and returns the JSON verdict. Always JUDGE_TEXT — by the
time the verdict pass runs, all the visual extraction has already happened.

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


class Judge:
    def __init__(
        self,
        config: LiteLLMConfig | None = None,
        *,
        prompt_template: str | None = None,
        describe_template: str | None = None,
        vision_available: bool | None = None,
    ) -> None:
        self.config = config or litellm_config()
        self.prompt_template = prompt_template or (_PROMPTS_DIR / "judge.md").read_text()
        self.describe_template = describe_template or (_PROMPTS_DIR / "judge_describe.md").read_text()
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
        )

        # ── Pass 2: score ────────────────────────────────────────────────
        verdict_alias = alias_for(Hat.JUDGE_TEXT)

        if artifact_text:
            artifact_block = artifact_text.strip()
        elif use_vision:
            artifact_block = "(image was described in the first pass; see description above)"
        else:
            artifact_block = "(no artifact text — judge from spec + description + coder output)"

        verdict_text = (
            f"{self.prompt_template}\n\n"
            "## Spec\n"
            f"{spec.strip()}\n\n"
            "## First-pass description\n"
            f"{description.strip()}\n\n"
            "## Last coder output\n"
            f"{(last_pi_output or '(empty)').strip()}\n\n"
            "## Artifact\n"
            f"{artifact_block}"
        )

        resp = await self._client.chat.completions.create(
            model=verdict_alias,
            messages=[{"role": "user", "content": verdict_text}],
            temperature=0.0,
        )
        raw = (resp.choices[0].message.content or "").strip()
        return _parse_verdict(raw, description=description)

    async def _describe(
        self,
        png_path: Path | None,
        artifact_text: str | None,
        spec: str,
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
        user_text = (
            f"{self.describe_template}\n\n"
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


def _parse_verdict(raw: str, *, description: str = "") -> JudgeVerdict:
    body = _FENCE_RE.sub("", raw).strip()
    try:
        obj = json.loads(body)
        score = obj.get("score")
        score_f = float(score) if score is not None else None
        return JudgeVerdict(
            score=score_f,
            critique=str(obj.get("critique", "")).strip(),
            done=bool(obj.get("done", False)),
            raw=raw,
            description=description,
        )
    except (json.JSONDecodeError, TypeError, ValueError) as e:
        log.warning("judge output did not parse as JSON (%s); raw=%r", e, raw[:200])
        return JudgeVerdict(
            score=None, critique=raw[:500], done=False, raw=raw, description=description
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
