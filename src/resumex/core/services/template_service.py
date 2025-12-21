import logging

from jinja2 import Environment, FileSystemLoader

from resumex.config.constants import Paths
from resumex.core.services import FileService, JsonService
from resumex.templates import Template


class TemplateService:

    TAG = "TemplateService"

    def __init__(self, file_service: FileService, json_service: JsonService):
        self.logger = logging.getLogger(TemplateService.TAG)
        self.file_service = file_service
        self.json_service = json_service
        self.env = Environment(loader=FileSystemLoader(Paths.TEMPLATES))

    def ls(self) -> list[str]:
        return Template.all()

    def render(self, template: Template = Template.DEFAULT):
        self.file_service.cleanup_dir(Paths.OUT_DIR)
        resume = self.json_service.validate()
        self.logger.info(f"Rendering template '{template.value}'")
        rendered = template.get(self.env).render(cv=resume)
        out_path = template.get_out_path()
        self.file_service.write(rendered, out_path)
        self.logger.info(f"Resume is available at {out_path}")
