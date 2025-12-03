import pytest

from tests.config import FIXTURES


@pytest.fixture
def sample_resume_json():
    path = FIXTURES.joinpath("resume.json")
    return path.read_text()


@pytest.fixture
def default_result():
    path = FIXTURES.joinpath("default.tex")
    return path.read_text().rstrip("\n")
