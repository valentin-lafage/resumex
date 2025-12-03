from enum import Enum
from typing import Literal, Union

from pydantic import BaseModel


class Level(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class LanguageLevel(str, Enum):
    BASIC = "Basic"
    PROFICIENT = "Proficient"
    FLUENT = "Fluent"
    NATIVE = "Native"


class LanguageSkill(BaseModel):
    name: str
    type: Literal["language"]
    level: LanguageLevel

    def __str__(self):
        return f"{self.name} ({self.level.value})"


class TechnicalSkill(BaseModel):
    name: str
    type: Literal["technical"]
    level: Level

    def __str__(self):
        return f"{self.name}"


Skill = Union[
    LanguageSkill,
    TechnicalSkill,
]
