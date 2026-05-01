from theloop.adapters.svg import SVGAdapter


def test_svg_preview_scales_artifact_to_viewport(tmp_path) -> None:
    SVGAdapter().prepare(tmp_path)

    html = (tmp_path / "index.html").read_text()

    assert "width: 92vw" in html
    assert "height: 92vh" in html
    assert "object-fit: contain" in html
