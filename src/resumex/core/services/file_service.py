import shutil
import logging

from click import File
from pathlib import Path

from resumex.config.constants import Paths


class FileService:

    TAG = "FileService"

    def __init__(self):
        self.logger = logging.getLogger(FileService.TAG)
        self.create_data_dir()

    def create_data_dir(self):
        Paths.DATA_DIR.mkdir(parents=True, exist_ok=True)

    def rmdir(self, dir: Path):
        if dir.exists() and dir.is_dir():
            shutil.rmtree(dir)
            self.logger.debug(f"Removed directory: {dir}")

    def cleanup_dir(self, dir: Path):
        self.rmdir(dir)
        dir.mkdir(parents=True, exist_ok=True)

    def read(self, file: Path) -> str:
        with open(file, "r") as f:
            return f.read()

    def write(self, content: str, destination: Path):
        with open(destination, "w") as f:
            f.write(content)

    def copy(self, source: Path | File, destination: Path):
        if isinstance(source, Path):
            shutil.copy(source, destination)
            return

        with open(destination, "wb") as dst:
            shutil.copyfileobj(source, dst)

    def get_extension(self, file: File) -> str:
        return Path(file.name).suffix
