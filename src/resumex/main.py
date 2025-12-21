import os
import logging
import logging.config

import resumex.core.cli.template
import resumex.core.cli.xp

from resumex.config import Paths
from resumex.core.cli import cli
from resumex.core.di import ServiceProvider
from resumex.templates.template import Template


def main():
    set_up_logging()
    init_dependency_providers()
    cli()


def set_up_logging():
    os.makedirs(Paths.LOGS_DIR, exist_ok=True)
    logging.config.fileConfig(
        Paths.CONFIG.joinpath("logging.conf"),
        defaults={"fname": Paths.LOGS_DIR.joinpath("resumex.log")},
    )


def init_dependency_providers():
    ServiceProvider()


if __name__ == "__main__":
    main()
