import logging

from click import File

from resumex.config import Paths
from resumex.core.services import FileService


class JsonService:

    TAG = "JsonService"

    def __init__(self, file_service: FileService):
        self.logger = logging.getLogger(JsonService.TAG)
        self.file_service = file_service

    def read(self):
        return self.file_service.read(Paths.JSON)

    def write(self, json: File):
        self.file_service.copy(json, Paths.JSON)
