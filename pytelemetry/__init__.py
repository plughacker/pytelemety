import logging.config
from logging import Logger
from typing import Optional

from pytelemetry.logger import LogConfig

_config = LogConfig()

logging.config.dictConfig(_config.dict())


def get_logger(name: Optional[str] = None) -> Logger:
    if not name:
        name = _config.LOGGER_NAME
    return logging.getLogger(name)
