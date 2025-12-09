from resumex.core.di import Provider
from resumex.core.services import (
    BackupService,
    FileService,
    JsonService,
    TemplateService,
)


class ServiceProvider(Provider):

    def __init__(self):
        super().__init__()
        self.file_service = FileService()
        self.backup_service = BackupService(self.file_service)
        self.json_service = JsonService(self.file_service)
        self.template_service = TemplateService(self.file_service, self.json_service)
