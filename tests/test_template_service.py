from resumex.core.services import FileService, TemplateService
from resumex.templates import Template


def test_template_service(tmp_path, sample_resume_json, default_result, mocker):
    out_path = tmp_path.joinpath("default.tex")

    ## FileService ##

    mock_file_service = mocker.Mock(spec=FileService)
    mock_file_service.read_json.return_value = sample_resume_json
    mock_file_service.write.side_effect = lambda content, path: path.write_text(content)
    mocker.patch("resumex.core.services.FileService", return_value=mock_file_service)

    ## TemplateService ##

    service = TemplateService(mock_file_service)
    mocker.patch.object(Template.DEFAULT, "get_out_path", return_value=out_path)
    service.render(template=Template.DEFAULT)

    assert out_path.exists()
    assert default_result == out_path.read_text()
