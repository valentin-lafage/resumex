import pytest

from pathlib import Path
from unittest.mock import MagicMock

from tests.config import Paths
from resumex.core.services import FileService, JsonService


@pytest.fixture(scope="session")
def seed(tmp_path_factory) -> Path:
    tmp_dir = tmp_path_factory.mktemp("seed")

    for src in Paths.SEED.iterdir():
        dst = tmp_dir.joinpath(src.name)
        dst.write_text(src.read_text())

    return tmp_dir


@pytest.fixture
def sample_resume_json() -> str:
    return Paths.RESUME_JSON.read_text()


@pytest.fixture
def default_result() -> str:
    path = Paths.DEFAULT_TEX
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
