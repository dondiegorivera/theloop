"""LiteLLM endpoint config and role → alias mapping.

The loop calls Qwen3.6 through the LiteLLM proxy at $LITELLM_BASE_URL.
LiteLLM holds the per-alias sampling presets (temperature, reasoning budget,
context); we deliberately depend only on alias names so the underlying model
can be swapped on the proxy without touching code.

See docs/spec.md §5 for the role table and docs/litellm-endpoints.md for the
LiteLLM config that backs each alias.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from enum import StrEnum

# .env is loaded by theloop.__init__ on package import.


class Hat(StrEnum):
    PLANNER = "planner"
    DIRECTOR = "director"
    CODER = "coder"
    WRITER = "writer"
    JUDGE_VISION = "judge_vision"
    JUDGE_TEXT = "judge_text"


_DEFAULT_ALIAS: dict[Hat, str] = {
    Hat.PLANNER: "Qwen3.6-Mesh-Thinking-Long",
    Hat.DIRECTOR: "Qwen3.6-Mesh-Structured",
    Hat.CODER: "Qwen3.6-Mesh-Code-Long",
    Hat.WRITER: "Qwen3.6-Mesh-Thinking-Long",
    Hat.JUDGE_VISION: "Qwen3.6-Mesh",
    # Judge-text reads the full artifact (e.g. a 25KB document.md) and must
    # return a single JSON object. Mesh-Structured is tuned for reliable
    # structured output; Mesh-Thinking exhausted its budget on reasoning
    # and emitted nothing once the artifact text was added to the prompt.
    Hat.JUDGE_TEXT: "Qwen3.6-Mesh-Structured",
}


def alias_for(hat: Hat) -> str:
    """Return the LiteLLM alias for a hat, honouring `THELOOP_MODEL_<HAT>` env."""
    return os.environ.get(f"THELOOP_MODEL_{hat.name}", _DEFAULT_ALIAS[hat])


@dataclass(frozen=True, slots=True)
class LiteLLMConfig:
    base_url: str
    api_key: str


def litellm_config() -> LiteLLMConfig:
    """Read LiteLLM proxy URL + master key from environment.

    Raises KeyError if either is missing — fail fast at startup.
    """
    return LiteLLMConfig(
        base_url=os.environ["LITELLM_BASE_URL"],
        api_key=os.environ["LITELLM_MASTER_KEY"],
    )


def main() -> None:
    cfg = litellm_config()
    print(f"LiteLLM base_url: {cfg.base_url}")
    print(f"LiteLLM key: {'set' if cfg.api_key else 'MISSING'}")
    print("Hat → alias:")
    for hat in Hat:
        print(f"  {hat.value:14s} → {alias_for(hat)}")


if __name__ == "__main__":
    main()
