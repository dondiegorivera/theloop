from pathlib import Path

from theloop.workspace import Workspace


def test_reconcile_external_write_from_run_root(tmp_path: Path) -> None:
    ws = Workspace.create(tmp_path, run_id="run")
    ws.begin_iteration(0)
    (ws.workspace_path / "artifact.svg").write_text("<svg>old</svg>")
    misplaced = ws.run_dir / "artifact.svg"
    misplaced.write_text("<svg>new</svg>")

    copied = ws.reconcile_external_writes([misplaced])

    assert copied == [(misplaced.resolve(), (ws.workspace_path / "artifact.svg").resolve())]
    assert (ws.workspace_path / "artifact.svg").read_text() == "<svg>new</svg>"


def test_reconcile_external_write_ignores_artifacts(tmp_path: Path) -> None:
    ws = Workspace.create(tmp_path, run_id="run")
    ws.begin_iteration(0)
    (ws.workspace_path / "artifact.svg").write_text("<svg>old</svg>")
    artifact = ws.artifact_dir(0) / "artifact.svg"
    artifact.write_text("<svg>render-copy</svg>")

    copied = ws.reconcile_external_writes([artifact])

    assert copied == []
    assert (ws.workspace_path / "artifact.svg").read_text() == "<svg>old</svg>"
