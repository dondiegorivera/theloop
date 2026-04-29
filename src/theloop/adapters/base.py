"""TaskAdapter ABC + shared result types.

An adapter encapsulates everything task-type-specific: how to scaffold the
initial workspace, how to sanity-check what pi produced, and how to turn it
into a PNG the judge can score. The Loop is otherwise task-agnostic.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class RuntimeCheckResult:
    ok: bool
    log: str  # informational on success; failure detail to feed back into the next plan


class TaskAdapter(ABC):
    name: str
    has_visual_artifact: bool = True

    def configure(self, frontmatter: dict[str, Any], spec_path: Path) -> None:
        """Read adapter-specific keys from the spec's YAML frontmatter.

        Default no-op. Adapters that need extra inputs (e.g. `doc` reads
        `source:`) override this. Called once by the CLI after the adapter
        is constructed and before `prepare()`.
        """
        del frontmatter, spec_path  # default impl intentionally ignores

    def extra_director_notes(self) -> str:
        """Run-specific notes appended to the static `_ADAPTER_NOTES`
        before the director sees them. Used by adapters whose guidance
        depends on configured state (e.g. `doc` listing the context manifest
        and the author's context_notes). Default empty.
        """
        return ""

    def artifact_text(self, workspace: Path) -> str | None:
        """Return the artifact's text content for the judge, or None.

        Adapters without a visual artifact should override this so the
        judge has something concrete to score against. Default None means
        the judge sees only spec + pi assistant text — fine for visual
        adapters (the screenshot carries the content) and for tasks where
        the judge cannot meaningfully evaluate raw file content.
        """
        del workspace
        return None

    @abstractmethod
    def prepare(self, workspace: Path) -> None:
        """Scaffold initial files. Called once before iter 0."""

    @abstractmethod
    def runtime_check(self, workspace: Path) -> RuntimeCheckResult:
        """Cheap, sync sanity check. Runs after pi edits, before render."""

    @abstractmethod
    async def render(self, workspace: Path, out_png: Path, renderer: "Renderer") -> None:
        """Produce a PNG of the current artifact state.

        Adapters that have no visual artifact should set
        `has_visual_artifact = False`; the Loop will not call this method
        for them.
        """


# Imported here only for the type annotation above; placed at the bottom to
# avoid a circular import (renderer.py does not depend on adapters).
from theloop.renderer import Renderer  # noqa: E402
