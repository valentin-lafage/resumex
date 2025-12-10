from resumex.core.services import TemplateService
from resumex.templates import Template


def test_default_rendering(
    tmp_path, json_service_mock, default_result, file_service_mock, mocker
):
    out_path = tmp_path.joinpath("default.tex")

    service = TemplateService(file_service_mock, json_service_mock)
    mocker.patch.object(Template.DEFAULT, "get_out_path", return_value=out_path)
    service.render(template=Template.DEFAULT)

    assert out_path.exists()
    assert default_result == out_path.read_text()
