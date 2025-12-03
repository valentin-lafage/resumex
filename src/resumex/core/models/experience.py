from datetime import date
from typing import List

from pydantic import BaseModel, Field

from resumex.core.models import Company


class Experience(BaseModel):
    company: Company
    position: str
    start_date: date
    end_date: date
    achievements: List[str] = Field(default_factory=list)
