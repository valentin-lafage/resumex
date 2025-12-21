from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field

from resumex.core.models import Company


class Experience(BaseModel):
    company: Company
    position: str
    start_date: date
    end_date: Optional[date] = None
    achievements: List[str] = Field(default_factory=list)

    @property
    def duration(self):
        fmt = "%b %Y"
        start = self.start_date.strftime(fmt)
        end = self.end_date.strftime(fmt) if self.end_date is not None else "Present"
        return f"{start} - {end}"
