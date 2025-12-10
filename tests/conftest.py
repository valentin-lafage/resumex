import pytest

from unittest.mock import MagicMock

from tests.config import FIXTURES
from resumex.core.services import FileService, JsonService


@pytest.fixture
def sample_resume_json():
    path = FIXTURES.joinpath("resume.json")
    return path.read_text()


@pytest.fixture
def default_result():
    path = FIXTURES.joinpath("default.tex")
    return path.read_text().rstrip("\n")


@pytest.fixture
def file_service_mock(mocker) -> MagicMock:
    mock = mocker.Mock(spec=FileService)
    mock.write.side_effect = lambda content, path: path.write_text(content)
    return mock


@pytest.fixture
def json_service_mock(sample_resume_json, mocker) -> MagicMock:
    mock = mocker.Mock(spec=JsonService)
    mock.read.return_value = sample_resume_json
    return mock
