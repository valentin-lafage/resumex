from resumex.core.di import Provider
from resumex.core.services import FileService, TemplateService


class ServiceProvider(Provider):

    @property
    def file_service(self) -> FileService:
        return self._file_service

    @property
    def template_service(self) -> TemplateService:
        return self._template_service

    def __init__(self):
        super().__init__()
        self._file_service = FileService()
        self._template_service = TemplateService(self._file_service)
