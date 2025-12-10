from enum import Enum
from pathlib import Path


class TestFile(Enum):
    RESUME_JSON = "resume.json"
    DEFAULT_TEX = "default.tex"


class Paths:
    ROOT = Path(__file__).parents[1]
    SEED = ROOT.joinpath("seed")

    RESUME_JSON = SEED.joinpath(TestFile.RESUME_JSON.value)
    DEFAULT_TEX = SEED.joinpath(TestFile.DEFAULT_TEX.value)
