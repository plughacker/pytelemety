import logging.config
from logging import Logger

from pytelemetry.logger import LogConfig

_config = LogConfig()

logging.config.dictConfig(_config.dict())


def create_logger(context_name: str) -> Logger:
    """
    Retorna um objeto logger configurado com as configurações definidas por LogConfig.

    Args:
        context_name (str): O nome do contexto para o qual o logger será usado.

    Returns:
        Logger: Um objeto logger configurado com base nas configurações fornecidas por LogConfig.

    Examples:
        logger = create_logger('YourClassName')
        logger.info("Esta é uma mensagem de informação.")
        logger.error("Este é um exemplo de mensagem de erro.", {'context': 123})
    """
    logger = logging.getLogger(_config.LOGGER_NAME)
    logger.name = context_name
    return logger
