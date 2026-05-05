import pytest

from theloop.adapters import get_adapter
from theloop.adapters.generic import GenericAdapter
from theloop.adapters.prose import ProseAdapter, count_words
from theloop.adapters.svg import SVGAdapter


def test_prose_adapter_registered() -> None:
    assert isinstance(get_adapter("prose"), ProseAdapter)


def test_adapter_judge_profiles() -> None:
    assert ProseAdapter().judge_profile() == "prose_quality"
    assert GenericAdapter().judge_profile() == "text_presence"
    assert SVGAdapter().judge_profile() == "visual_presence"


def test_prose_prepare_and_artifact_text_use_configured_artifact(tmp_path) -> None:
    adapter = ProseAdapter()
    adapter.configure({"artifact": "drafts/scene.md"}, tmp_path / "spec.md")
    adapter.prepare(tmp_path)

    artifact_path = tmp_path / "drafts" / "scene.md"
    assert artifact_path.exists()
    assert (tmp_path / "README.md").exists()

    artifact_path.write_text("The suitcase stayed open on the bed.\n")
    artifact = adapter.artifact_text(tmp_path)

    assert artifact is not None
    assert "### drafts/scene.md" in artifact
    assert "The suitcase stayed open" in artifact
    assert "README.md" not in artifact


def test_prose_runtime_check_rejects_placeholder(tmp_path) -> None:
    adapter = ProseAdapter()
    adapter.prepare(tmp_path)

    result = adapter.runtime_check(tmp_path)

    assert not result.ok
    assert "placeholder" in result.log


def test_prose_runtime_check_word_count_passes_inside_tolerance(tmp_path) -> None:
    adapter = ProseAdapter()
    adapter.configure(
        {"artifact": "scene.md", "target_words": 200, "word_tolerance": 20},
        tmp_path / "spec.md",
    )
    adapter.prepare(tmp_path)
    (tmp_path / "scene.md").write_text("word " * 180)

    result = adapter.runtime_check(tmp_path)

    assert result.ok
    assert "180 words" in result.log


def test_prose_runtime_check_word_count_fails_outside_tolerance(tmp_path) -> None:
    adapter = ProseAdapter()
    adapter.configure(
        {"artifact": "scene.md", "target_words": 200, "word_tolerance": 20},
        tmp_path / "spec.md",
    )
    adapter.prepare(tmp_path)
    (tmp_path / "scene.md").write_text("word " * 150)

    result = adapter.runtime_check(tmp_path)

    assert not result.ok
    assert "outside target 200+/-20" in result.log


def test_prose_runtime_check_banned_phrases_are_case_insensitive(tmp_path) -> None:
    adapter = ProseAdapter()
    adapter.configure(
        {"artifact": "scene.md", "banned_phrases": ["she felt"]},
        tmp_path / "spec.md",
    )
    adapter.prepare(tmp_path)
    (tmp_path / "scene.md").write_text("She Felt the latch click.\n")

    result = adapter.runtime_check(tmp_path)

    assert not result.ok
    assert "banned phrases: she felt" in result.log


def test_prose_runtime_check_required_prefix(tmp_path) -> None:
    adapter = ProseAdapter()
    adapter.configure(
        {"artifact": "story.md", "required_prefix": ">be me"},
        tmp_path / "spec.md",
    )
    adapter.prepare(tmp_path)
    (tmp_path / "story.md").write_text("be me, Qwen 3.6\n")

    result = adapter.runtime_check(tmp_path)

    assert not result.ok
    assert "missing required prefix" in result.log


def test_prose_config_rejects_absolute_or_parent_artifact_paths(tmp_path) -> None:
    adapter = ProseAdapter()
    with pytest.raises(ValueError, match="relative"):
        adapter.configure({"artifact": "/tmp/scene.md"}, tmp_path / "spec.md")

    with pytest.raises(ValueError, match="parent"):
        adapter.configure({"artifact": "../scene.md"}, tmp_path / "spec.md")


def test_prose_config_rejects_invalid_scalar_types(tmp_path) -> None:
    adapter = ProseAdapter()
    with pytest.raises(ValueError, match="target_words"):
        adapter.configure({"target_words": "200"}, tmp_path / "spec.md")

    with pytest.raises(ValueError, match="banned_phrases"):
        adapter.configure({"banned_phrases": "she felt"}, tmp_path / "spec.md")


def test_count_words_handles_contractions_and_hyphenation() -> None:
    assert count_words("can't stop the slow-moving suitcase") == 5
