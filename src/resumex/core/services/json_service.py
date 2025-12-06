import logging

from click import File

from resumex.config import Paths
from resumex.core.services import FileService


class JsonService:

    TAG = "JsonService"

    def __init__(self, file_service: FileService):
        self._logger = logging.getLogger(JsonService.TAG)
        self._file_service = file_service

    def read(self):
        return self._file_service.read(Paths.JSON)

    def write(self, json: File):
        self._file_service.copy(json, Paths.JSON)
