from enum import Enum
from pathlib import Path

from jinja2 import Environment, Template as JinjaTemplate

from resumex.config.constants import Paths


class Template(Enum):
    DEFAULT = "default.tex"

    @classmethod
    def from_index(cls, index: int) -> "Template":
        return list(cls)[index]

    @classmethod
    def all(cls) -> list[str]:
        return [template.value for template in Template]

    def get(self, env: Environment) -> JinjaTemplate:
        return env.get_template(self.value)

    def get_out_path(self) -> Path:
        return Paths.OUT_DIR.joinpath(self.value)
