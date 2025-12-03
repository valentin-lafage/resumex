from platformdirs import user_log_dir
from pathlib import Path


class PkgInfo:
    AUTHOR = "vlafage"
    NAME = "resumex"


class Paths:
    CONFIG = Path(__file__).parent
    LOGS = Path(user_log_dir(PkgInfo.NAME, PkgInfo.AUTHOR))
