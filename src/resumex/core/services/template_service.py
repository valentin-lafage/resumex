import logging

from jinja2 import Environment, FileSystemLoader

from resumex.config.constants import Paths
from resumex.core.models import Resume
from resumex.core.services import FileService
from resumex.templates import Template


class TemplateService:

    TAG = "TemplateService"

    def __init__(self, file_service: FileService):
        self._logger = logging.getLogger(TemplateService.TAG)
        self._file_service = file_service
        self._env = Environment(loader=FileSystemLoader(Paths.TEMPLATES))

    def render(self, template: Template = Template.DEFAULT):
        resume = Resume.model_validate_json(self._file_service.read_json())
        self._logger.info(f"Rendering template '{template.value}'")
        rendered = template.get(self._env).render(cv=resume)
        out_path = template.get_out_path()
        self._file_service.write(rendered, out_path)
        self._logger.info(f"Resume is available at {out_path}")
