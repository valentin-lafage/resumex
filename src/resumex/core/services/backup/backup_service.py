import logging

from pathlib import Path

from resumex.config.constants import Paths
from resumex.core.services import FileService
from .backup import Backup


class BackupService:

    TAG = "BackupService"

    SUPPORTED_FILE_EXT = [".json", ".tex"]

    @property
    def src(self) -> Path:
        return Paths.DATA_DIR

    @property
    def dst(self) -> Path:
        return Paths.BACKUP_DIR

    def __init__(self, file_service: FileService):
        self.logger = logging.getLogger(BackupService.TAG)
        self.file_service = file_service
        if self.dst.exists():
            self.cleanup()

    def get_files_to_backup(self) -> list[Backup]:
        return [Backup(p) for p in self.src.rglob("*") if self.should_backup(p)]

    def should_backup(self, src: Path) -> bool:
        return src.is_file() and src.suffix in BackupService.SUPPORTED_FILE_EXT

    def backup(self):
        content = self.get_files_to_backup()
        if not content:
            return
        backup = self.create_backup_dir()
        self.logger.debug(f"Backing up files into '{backup.path}'")
        for file in content:
            src = file.path
            dst = backup.path.joinpath(src.name)
            self.file_service.copy(src, dst)

    def create_backup_dir(self) -> Backup:
        dir_path = self.dst.joinpath(Backup.construct_dirname())
        dir_path.mkdir(parents=True)
        return Backup(dir_path)

    def get_backups(self) -> list[Backup]:
        return [Backup(p) for p in self.dst.iterdir() if p.is_dir()]

    def get_old_backups(self) -> list[Backup]:
        return [b for b in self.get_backups() if b.is_too_old()]

    def cleanup(self):
        paths = (old.path for old in self.get_old_backups())
        for path in paths:
            self.logger.debug(f"Removing old backup '{path.name}'")
            self.file_service.rmdir(path)
