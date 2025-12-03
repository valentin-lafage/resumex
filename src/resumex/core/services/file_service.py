import shutil
import logging

from pathlib import Path

from resumex.config.constants import Paths


class FileService:

    TAG = "FileService"

    def __init__(self):
        self._logger = logging.getLogger(FileService.TAG)
        self.create_data_dir()
        self.cleanup_dir(Paths.OUT_DIR)

    def create_data_dir(self):
        Paths.DATA_DIR.mkdir(parents=True, exist_ok=True)

    def cleanup_dir(self, dir: Path):
        if dir.exists() and dir.is_dir():
            shutil.rmtree(dir)
            self._logger.info(f"Removed directory: {dir}")
        dir.mkdir(parents=True, exist_ok=True)

    def read_json(self):
        return self.read(Paths.JSON)

    def read(self, file: Path) -> str:
        with open(file, "r") as f:
            return f.read()

    def write(self, content: str, destination: Path):
        with open(destination, "w") as f:
            f.write(content)
