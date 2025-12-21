import pytest

from pathlib import Path

from tests.config import Paths
from resumex.core.services import (
    BackupService,
    FileService,
    JsonService,
    TemplateService,
)


@pytest.fixture
def seed(tmp_path) -> Path:
    for src in Paths.SEED.iterdir():
        dst = tmp_path.joinpath(src.name)
        dst.write_text(src.read_text())
    return tmp_path


@pytest.fixture
def sample_resume_json() -> str:
    return Paths.RESUME_JSON.read_text()


@pytest.fixture
def default_result() -> str:
    path = Paths.DEFAULT_TEX
    return path.read_text().rstrip("\n")


## Services ##


@pytest.fixture
def backup_service(file_service, seed, mocker) -> BackupService:
    cls = "resumex.core.services.BackupService"
    src = seed
    dst = seed.joinpath("backup")
    mocker.patch(f"{cls}.src", return_value=src, new_callable=mocker.PropertyMock)
    mocker.patch(f"{cls}.dst", return_value=dst, new_callable=mocker.PropertyMock)
    return BackupService(file_service)


@pytest.fixture
def file_service():
    return FileService()


@pytest.fixture
def template_service(file_service, json_service):
    return TemplateService(file_service, json_service)


@pytest.fixture
def json_service(file_service, sample_resume_json, mocker) -> JsonService:
    service = JsonService(file_service)
    mocker.patch.object(service, "read", return_value=sample_resume_json)
    return service
