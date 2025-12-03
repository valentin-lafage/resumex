import os
import logging
import logging.config

from resumex.config import Paths
from resumex.core.di import ServiceProvider


def main():
    set_up_logging()
    init_dependency_providers()


def set_up_logging():
    os.makedirs(Paths.LOGS, exist_ok=True)
    logging.config.fileConfig(
        Paths.CONFIG.joinpath("logging.conf"),
        defaults={"fname": str(Paths.LOGS.joinpath("resumex.log"))},
    )


def init_dependency_providers():
    ServiceProvider()


if __name__ == "__main__":
    main()
