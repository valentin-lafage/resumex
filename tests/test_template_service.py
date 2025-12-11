from resumex.templates import Template


def test_default_rendering(tmp_path, template_service, default_result, mocker):
    """
    Should produce a tex file matching the default template.
    """
    out_path = tmp_path.joinpath("default.tex")
    mocker.patch.object(Template.DEFAULT, "get_out_path", return_value=out_path)
    template_service.render()

    assert out_path.exists()
    assert default_result == out_path.read_text()
