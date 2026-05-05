import json

from theloop.reporter import build_html_report


def _event(kind: str, *, iter: int | None = None, payload: dict | None = None) -> str:
    return json.dumps(
        {
            "ts": "2026-05-01T00:00:00+00:00",
            "iter": iter,
            "kind": kind,
            "payload": payload or {},
        }
    )


def test_report_links_judged_text_artifact(tmp_path) -> None:
    run_dir = tmp_path / "run"
    artifact_dir = run_dir / "artifacts" / "iter-0"
    artifact_dir.mkdir(parents=True)
    (artifact_dir / "artifact.txt").write_text("### scene.txt\n\nThe suitcase stayed open.\n")
    (run_dir / "events.jsonl").write_text(
        "\n".join(
            [
                _event("run_start", payload={"adapter": "generic"}),
                _event("plan_end", iter=0, payload={"intent": "write scene"}),
                _event("runtime_check", iter=0, payload={"ok": True, "log": "ok"}),
                _event(
                    "judge_end",
                    iter=0,
                    payload={
                        "score": 0.7,
                        "critique": "revise",
                        "done": False,
                        "hard_failures": ["word count outside target"],
                        "dimensions": {"specificity": 0.75},
                    },
                ),
                _event("run_end", payload={"reason": "max_iters"}),
            ]
        )
    )

    report = build_html_report(run_dir).read_text()

    assert 'href="artifacts/iter-0/artifact.txt"' in report
    assert "judged artifact" in report
    assert "word count outside target" in report
    assert "specificity" in report
    assert "0.75" in report
