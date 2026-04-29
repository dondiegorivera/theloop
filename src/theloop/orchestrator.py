"""Orchestrator — planner + director hats, both backed by agno.

Two agno `Agent` instances, each pointed at the LiteLLM proxy via
`OpenAIChat(base_url=..., api_key=...)`. The "hat" is just the model alias
the agent was constructed with — see `theloop.models.Hat` for the mapping.

In phase 2 we'll likely add a `critic` hat and possibly memory / tool
registration. The two-method surface here is deliberately minimal so loop.py
doesn't have to know about agno internals.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from pydantic import BaseModel, Field

from theloop.models import Hat, LiteLLMConfig, alias_for, litellm_config

log = logging.getLogger(__name__)

_PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
_FENCE_RE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$", re.MULTILINE)
# Some thinking-mode models still emit <think>...</think> blocks even when
# the proxy enforces a thinking budget. Strip them defensively.
_THINK_RE = re.compile(r"<think>.*?</think>\s*", re.DOTALL)


@dataclass(frozen=True, slots=True)
class PlanResult:
    spec: str
    intent: str


class _PlannerOutput(BaseModel):
    spec: str = Field(..., description="The full updated spec markdown.")
    intent: str = Field(..., description="One short paragraph; the iteration's intent.")


class Orchestrator:
    def __init__(self, config: LiteLLMConfig | None = None) -> None:
        cfg = config or litellm_config()
        self._cfg = cfg

        planner_model = OpenAIChat(
            id=alias_for(Hat.PLANNER),
            base_url=cfg.base_url,
            api_key=cfg.api_key,
        )
        director_model = OpenAIChat(
            id=alias_for(Hat.DIRECTOR),
            base_url=cfg.base_url,
            api_key=cfg.api_key,
        )

        self._planner_prompt = (_PROMPTS_DIR / "planner.md").read_text()
        self._director_prompt = (_PROMPTS_DIR / "director.md").read_text()

        self._planner = Agent(
            name="planner",
            model=planner_model,
            instructions=[self._planner_prompt],
            markdown=False,
        )
        self._director = Agent(
            name="director",
            model=director_model,
            instructions=[self._director_prompt],
            markdown=False,
        )

    # ── planner hat ───────────────────────────────────────────────────────

    async def plan(self, spec: str, critique: str | None) -> PlanResult:
        """Return the next-iteration spec + intent.

        Parses the model's JSON output. Falls back to a best-effort regex
        extraction on JSON failure rather than raising, so the loop can
        keep going with a degraded plan.
        """
        prev = critique.strip() if critique else "(none — first iteration)"
        user = (
            "## Spec\n"
            f"{spec.strip()}\n\n"
            "## Previous critique\n"
            f"{prev}\n"
        )
        resp = await self._planner.arun(user)
        raw = (resp.content or "").strip()
        return _parse_plan(raw, fallback_spec=spec)

    # ── director hat ──────────────────────────────────────────────────────

    async def direct(
        self,
        intent: str,
        workspace: Path,
        adapter_notes: str,
    ) -> str:
        """Turn an iteration intent into a prompt for pi."""
        inventory = _workspace_inventory(workspace)
        user = (
            "## Intent\n"
            f"{intent.strip()}\n\n"
            "## Workspace inventory\n"
            f"{inventory}\n\n"
            "## Adapter notes\n"
            f"{adapter_notes.strip()}\n"
        )
        resp = await self._director.arun(user)
        text = (resp.content or "").strip()
        text = _THINK_RE.sub("", text).strip()
        return text


# ── helpers ──────────────────────────────────────────────────────────────────


def _parse_plan(raw: str, *, fallback_spec: str) -> PlanResult:
    body = _THINK_RE.sub("", raw)
    body = _FENCE_RE.sub("", body).strip()
    try:
        obj = json.loads(body)
        return PlanResult(
            spec=str(obj["spec"]),
            intent=str(obj["intent"]).strip(),
        )
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        log.warning(
            "planner output did not parse as JSON (%s); using fallback. raw[:200]=%r",
            e,
            raw[:200],
        )
        # Best-effort: keep prior spec, treat raw text as the intent.
        intent = raw.strip()[:600] or "(planner produced no usable output)"
        return PlanResult(spec=fallback_spec, intent=intent)


def _workspace_inventory(workspace: Path, *, max_entries: int = 30) -> str:
    if not workspace.exists():
        return "(workspace does not exist yet)"
    entries: list[str] = []
    for p in sorted(workspace.rglob("*")):
        if ".git" in p.parts:
            continue
        if p.is_dir():
            continue
        rel = p.relative_to(workspace)
        try:
            size = p.stat().st_size
        except OSError:
            size = -1
        entries.append(f"- {rel} ({size}B)")
        if len(entries) >= max_entries:
            entries.append(f"- ... ({max_entries}+ files; truncated)")
            break
    if not entries:
        return "(empty workspace)"
    return "\n".join(entries)


# ── manual smoke test ───────────────────────────────────────────────────────


async def _smoke() -> None:
    """Usage: python -m theloop.orchestrator

    Round-trips plan() and direct() against the live LiteLLM proxy using
    the pelican spec from the worked example.
    """
    import tempfile

    from theloop.adapters.svg import SVGAdapter
    from theloop.workspace import Workspace

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    spec = (
        "---\n"
        "adapter: svg\n"
        "max_iters: 8\n"
        "---\n"
        "Draw an SVG of a pelican riding a bicycle. The pelican should be "
        "recognizable, the bike should have two wheels and a frame, and the "
        "composition should suggest motion."
    )

    orch = Orchestrator()
    print(f"planner alias:  {alias_for(Hat.PLANNER)}")
    print(f"director alias: {alias_for(Hat.DIRECTOR)}")

    print("\n=== plan() iter 0 ===")
    plan0 = await orch.plan(spec, critique=None)
    print(f"intent: {plan0.intent[:300]}")
    print(f"spec len: {len(plan0.spec)} chars (input was {len(spec)})")
    assert plan0.intent, "planner returned empty intent"
    assert "pelican" in plan0.spec.lower(), "spec should still mention pelican"

    with tempfile.TemporaryDirectory(prefix="theloop-orch-") as tmp:
        ws = Workspace.create(Path(tmp), slug="orch-smoke")
        SVGAdapter().prepare(ws.workspace_path)

        print("\n=== direct() iter 0 ===")
        adapter_notes = (
            "Edit `artifact.svg` only. Do not touch `index.html` or "
            "`README.md`. The SVG must parse as XML."
        )
        pi_prompt = await orch.direct(
            intent=plan0.intent,
            workspace=ws.workspace_path,
            adapter_notes=adapter_notes,
        )
        print(f"pi prompt ({len(pi_prompt)} chars):\n---\n{pi_prompt[:800]}\n---")
        assert pi_prompt, "director returned empty prompt"
        assert "artifact.svg" in pi_prompt.lower(), "director should mention the target file"

    print("\n=== plan() iter 1 with fake critique ===")
    plan1 = await orch.plan(
        plan0.spec,
        critique=(
            "The pelican is unrecognizable — appears as a gray blob. "
            "The bicycle has only one wheel. Add a distinguishable beak "
            "and a rear wheel."
        ),
    )
    print(f"intent: {plan1.intent[:300]}")
    assert plan1.intent != plan0.intent, "iter 1 intent should differ from iter 0"

    print("\n✓ orchestrator round-trip ok")


if __name__ == "__main__":
    import asyncio

    asyncio.run(_smoke())
