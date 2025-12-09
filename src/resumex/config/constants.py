from platformdirs import user_log_dir, user_data_dir
from pathlib import Path
from importlib.resources import files


class PkgInfo:
    AUTHOR = "vlafage"
    NAME = "resumex"


class Paths:
    # - Linux: ~/.local/state/resumex/logs
    LOGS_DIR = Path(user_log_dir(PkgInfo.NAME, PkgInfo.AUTHOR))
    # - Linux: ~/.local/share/resumex
    DATA_DIR = Path(user_data_dir(PkgInfo.NAME, PkgInfo.AUTHOR))

    ROOT = Path(files("resumex"))

    # Paths relative to the package
    CONFIG = ROOT.joinpath("config")
    TEMPLATES = ROOT.joinpath("templates")

    # Paths relative to the user data directory
    BACKUP_DIR = DATA_DIR.joinpath("backup")
    JSON = DATA_DIR.joinpath("resume.json")
    OUT_DIR = DATA_DIR.joinpath("out")
