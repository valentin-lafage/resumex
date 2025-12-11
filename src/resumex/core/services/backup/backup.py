from dataclasses import dataclass
from datetime import datetime as dt, timedelta
from pathlib import Path


@dataclass
class Backup:
    path: Path

    DIRNAME_PREFIX = "backup_"
    DIRNAME_FORMAT = "%Y%m%d_%H%M%S"
    RETENTION_TIME = timedelta(days=7)

    @property
    def last_modified(self) -> int:
        return dt.fromtimestamp(self.path.stat().st_mtime)

    @property
    def time(self) -> int:
        return self.path.stem.removeprefix(Backup.DIRNAME_PREFIX)

    @property
    def content(self) -> list[Path]:
        return list(self.path.iterdir())

    def is_too_old(self) -> bool:
        return self.last_modified < (dt.now() - Backup.RETENTION_TIME)

    @classmethod
    def construct_dirname(cls) -> str:
        return cls.DIRNAME_PREFIX + dt.now().strftime(cls.DIRNAME_FORMAT)
