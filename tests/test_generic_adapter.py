from theloop.adapters.generic import GenericAdapter


def test_generic_artifact_text_includes_text_outputs(tmp_path) -> None:
    adapter = GenericAdapter()
    adapter.prepare(tmp_path)
    (tmp_path / "scene.txt").write_text("They folded the map around the stain.\n")

    artifact = adapter.artifact_text(tmp_path)

    assert artifact is not None
    assert "### scene.txt" in artifact
    assert "They folded the map" in artifact
    assert "Generic task workspace" not in artifact


def test_generic_artifact_text_includes_code_outputs(tmp_path) -> None:
    adapter = GenericAdapter()
    adapter.prepare(tmp_path)
    (tmp_path / "solver.py").write_text("def solve():\n    return 42\n")

    artifact = adapter.artifact_text(tmp_path)

    assert artifact is not None
    assert "### solver.py" in artifact
    assert "def solve()" in artifact


def test_generic_artifact_text_returns_none_without_created_text(tmp_path) -> None:
    adapter = GenericAdapter()
    adapter.prepare(tmp_path)

    assert adapter.artifact_text(tmp_path) is None
