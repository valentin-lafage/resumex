import os
import time
import pytest

from datetime import datetime as dt

from resumex.core.services.backup import Backup


def test_backup_srcs_count(backup_service):
    """
    There should be only 2 files to backup.
    Only regular files matching '.json' or '.tex' extension should be included.
    """
    backup_service.src.joinpath("dir").mkdir()
    backup_service.src.joinpath("file.txt").touch()
    files_count = len(list(backup_service.src.iterdir()))
    assert files_count == 4
    assert len(backup_service.get_files_to_backup()) == 2


def test_backup_mkdir(backup_service):
    """
    The backup base directory should be created from its child.
    """
    dir = backup_service.dst
    assert not dir.exists()
    bk = backup_service.create_backup_dir()
    assert bk.path.parent == dir
    assert dir.exists()


def test_backup(backup_service):
    """
    The backup should hold 2 files.
    """
    assert not backup_service.dst.exists()
    backup_service.backup()
    backups = backup_service.get_backups()
    backup_files = [f for bk in backups for f in bk.content]
    assert len(backup_files) == 2
    for f in backup_files:
        assert f.suffix in [".json", ".tex"]


def test_two_backups(backup_service):
    """
    Expecting two backup directories, each containing 2 files.
    """
    backup_service.backup()
    assert len(backup_service.get_backups()) == 1
    time.sleep(1)
    backup_service.backup()

    backups = backup_service.get_backups()
    assert len(backups) == 2
    for bk in backups:
        assert len(bk.content) == 2


def test_two_backups_at_once_raises_file_exists_error(backup_service):
    """
    Creating two backups at the same time should produce a conflict in the
    filename.
    """
    backup_service.backup()
    with pytest.raises(FileExistsError):
        backup_service.backup()


def test_backup_retention(backup_service):
    """
    There should be 1 backup to dispose when 1 backup is outdated.
    """
    backup_service.backup()
    assert len(backup_service.get_old_backups()) == 0
    for bk in backup_service.dst.iterdir():
        outatime = (dt.now() - (Backup.RETENTION_TIME)).timestamp()
        os.utime(bk, (outatime, outatime))
    assert len(backup_service.get_old_backups()) == 1
