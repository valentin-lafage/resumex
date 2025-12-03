from typing import List

from pydantic import BaseModel, Field


class Education(BaseModel):
    institution: str
    degree: str
    year: int
    achievements: List[str] = Field(default_factory=list)
