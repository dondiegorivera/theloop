"""ProseAdapter — generate and iteratively refine one prose artifact.

This is for new writing tasks: scenes, short stories, scripts, concepts, or
other prose artifacts that do not start from an existing source document.
Unlike `generic`, this adapter defines one canonical artifact file so the
judge and report can track the actual draft across iterations.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

from theloop.adapters.base import RuntimeCheckResult, TaskAdapter
from theloop.renderer import Renderer

log = logging.getLogger(__name__)

_DEFAULT_ARTIFACT = "artifact.md"
_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*")

_README_TEMPLATE = """\
# Prose task workspace

The prose artifact lives at `{artifact}`. Edit that file directly. Do not
create alternate drafts or side files unless the spec explicitly asks for
them; theloop judges the canonical artifact file.

Tools available: read, write, edit, bash. There is no rendered preview.
"""

_PLACEHOLDER = """\
Draft goes here. Replace this placeholder with the requested prose artifact.
"""


class ProseAdapter(TaskAdapter):
    name = "prose"
    has_visual_artifact = False

    def __init__(self) -> None:
        self.artifact_name = _DEFAULT_ARTIFACT
        self.target_words: int | None = None
        self.word_tolerance: int | None = None
        self.banned_phrases: list[str] = []
        self.required_prefix: str | None = None

    def configure(self, frontmatter: dict[str, Any], spec_path: Path) -> None:
        del spec_path
        artifact = frontmatter.get("artifact", _DEFAULT_ARTIFACT)
        if not isinstance(artifact, str) or not artifact.strip():
            raise ValueError("prose `artifact:` must be a non-empty relative path")
        self.artifact_name = _validate_artifact_path(artifact)

        self.target_words = _optional_int(frontmatter, "target_words")
        self.word_tolerance = _optional_int(frontmatter, "word_tolerance")
        if self.word_tolerance is not None and self.word_tolerance < 0:
            raise ValueError("prose `word_tolerance:` must be >= 0")

        banned = frontmatter.get("banned_phrases") or []
        if not isinstance(banned, list) or not all(isinstance(x, str) for x in banned):
            raise ValueError("prose `banned_phrases:` must be a list of strings")
        self.banned_phrases = [x for x in (s.strip() for s in banned) if x]

        prefix = frontmatter.get("required_prefix")
        if prefix is not None and not isinstance(prefix, str):
            raise ValueError("prose `required_prefix:` must be a string")
        self.required_prefix = prefix.strip() if isinstance(prefix, str) and prefix.strip() else None

    @property
    def artifact_path(self) -> Path:
        return Path(self.artifact_name)

    def prepare(self, workspace: Path) -> None:
        artifact = workspace / self.artifact_path
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text(_PLACEHOLDER)
        (workspace / "README.md").write_text(
            _README_TEMPLATE.format(artifact=self.artifact_name)
        )
        log.debug("prose scaffold written to %s", workspace)

    def runtime_check(self, workspace: Path) -> RuntimeCheckResult:
        artifact = workspace / self.artifact_path
        if not artifact.exists():
            return RuntimeCheckResult(ok=False, log=f"{self.artifact_name} missing")
        text = artifact.read_text()
        stripped = text.strip()
        if not stripped:
            return RuntimeCheckResult(ok=False, log=f"{self.artifact_name} is empty")
        if stripped == _PLACEHOLDER.strip():
            return RuntimeCheckResult(
                ok=False,
                log=f"{self.artifact_name} still contains the scaffold placeholder",
            )

        failures: list[str] = []
        word_count = count_words(text)
        if self.target_words is not None:
            tolerance = self.word_tolerance or 0
            lo = self.target_words - tolerance
            hi = self.target_words + tolerance
            if word_count < lo or word_count > hi:
                failures.append(
                    f"word count {word_count} outside target {self.target_words}"
                    f"+/-{tolerance}"
                )

        lowered = text.lower()
        banned_hits = [
            phrase for phrase in self.banned_phrases
            if phrase.lower() in lowered
        ]
        if banned_hits:
            failures.append("banned phrases: " + ", ".join(banned_hits[:5]))

        if self.required_prefix is not None and not stripped.startswith(self.required_prefix):
            failures.append(f"missing required prefix {self.required_prefix!r}")

        summary = f"{self.artifact_name} ({word_count} words, {len(text)} chars)"
        if failures:
            return RuntimeCheckResult(ok=False, log=f"{summary}; " + "; ".join(failures))
        return RuntimeCheckResult(ok=True, log=f"{summary}; prose checks passed")

    async def render(self, workspace: Path, out_png: Path, renderer: Renderer) -> None:
        del workspace, out_png, renderer
        raise NotImplementedError("ProseAdapter has no visual artifact")

    def artifact_text(self, workspace: Path) -> str | None:
        artifact = workspace / self.artifact_path
        if not artifact.exists():
            return None
        text = artifact.read_text()
        words = count_words(text)
        return (
            f"### {self.artifact_name} ({words} words, {len(text)} chars)\n\n"
            f"{text}\n"
        )

    def judge_profile(self) -> str:
        return "prose_quality"

    def extra_director_notes(self) -> str:
        parts = [
            f"The canonical prose artifact is `{self.artifact_name}`. "
            "Edit that file directly and do not create alternate drafts unless "
            "the spec explicitly asks for them."
        ]
        if self.target_words is not None:
            tolerance = self.word_tolerance or 0
            parts.append(
                f"Target word count: {self.target_words} +/- {tolerance} words."
            )
        if self.banned_phrases:
            parts.append(
                "Avoid these banned phrases exactly: "
                + ", ".join(f"`{phrase}`" for phrase in self.banned_phrases)
                + "."
            )
        if self.required_prefix:
            parts.append(f"The artifact must start with `{self.required_prefix}`.")
        return " ".join(parts)


def count_words(text: str) -> int:
    return len(_WORD_RE.findall(text))


def _optional_int(frontmatter: dict[str, Any], key: str) -> int | None:
    value = frontmatter.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"prose `{key}:` must be an integer")
    if value < 0:
        raise ValueError(f"prose `{key}:` must be >= 0")
    return value


def _validate_artifact_path(value: str) -> str:
    path = Path(value.strip())
    if path.is_absolute():
        raise ValueError("prose `artifact:` must be relative")
    if not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError("prose `artifact:` must not contain empty or parent path parts")
    return path.as_posix()
