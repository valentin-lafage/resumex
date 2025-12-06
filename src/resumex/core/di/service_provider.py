from resumex.core.di import Provider
from resumex.core.services import FileService, JsonService, TemplateService


class ServiceProvider(Provider):

    @property
    def file_service(self) -> FileService:
        return self._file_service

    @property
    def json_service(self) -> JsonService:
        return self._json_service

    @property
    def template_service(self) -> TemplateService:
        return self._template_service

    def __init__(self):
        super().__init__()
        self._file_service = FileService()
        self._json_service = JsonService(self._file_service)
        self._template_service = TemplateService(self._file_service, self._json_service)
