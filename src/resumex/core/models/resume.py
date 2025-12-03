from typing import List

from pydantic import BaseModel, Field

from resumex.core.models import Contact, Education, Experience, Skill


class Resume(BaseModel):
    contact: Contact
    educations: List[Education] = Field(default_factory=list)
    experiences: List[Experience] = Field(default_factory=list)
    skills: List[Skill] = Field(default_factory=list)
