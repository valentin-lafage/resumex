from resumex.core.services import FileService, JsonService, TemplateService
from resumex.templates import Template


def test_template_service(tmp_path, sample_resume_json, default_result, mocker):
    out_path = tmp_path.joinpath("default.tex")

    ## FileService ##

    mock_file_service = mocker.Mock(spec=FileService)
    mock_file_service.write.side_effect = lambda content, path: path.write_text(content)

    ## JsonService ##

    mock_json_service = mocker.Mock(spec=JsonService)
    mock_json_service.read.return_value = sample_resume_json

    ## TemplateService ##

    service = TemplateService(mock_file_service, mock_json_service)
    mocker.patch.object(Template.DEFAULT, "get_out_path", return_value=out_path)
    service.render(template=Template.DEFAULT)

    assert out_path.exists()
    assert default_result == out_path.read_text()
