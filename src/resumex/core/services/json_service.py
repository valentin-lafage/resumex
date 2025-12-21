import logging

from click import File

from resumex.config import Paths
from resumex.core.models import Experience, Resume
from resumex.core.services import FileService


class JsonService:

    TAG = "JsonService"

    def __init__(self, file_service: FileService):
        self.logger = logging.getLogger(JsonService.TAG)
        self.file_service = file_service

    def validate(self) -> Resume:
        return Resume.model_validate_json(self.read())

    def get_experiences(self, resume: Resume) -> list[Experience]:
        return sorted(resume.experiences, key=lambda xp: xp.start_date, reverse=True)

    def add_experience(self, xp: Experience) -> str:
        resume = self.validate()
        resume.experiences.append(xp)
        self.write(resume)

    def read(self) -> str:
        return self.file_service.read(Paths.JSON)

    def write(self, resume: Resume):
        self.file_service.write(resume.model_dump_json(indent=2), Paths.JSON)

    def copy(self, json: File):
        self.file_service.copy(json, Paths.JSON)
