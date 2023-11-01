import logging.config
from logging import Logger
from typing import Optional

from pytelemetry.context import PyTelemetryContextVar
from pytelemetry.logger import LogConfig

_config = LogConfig()

logging.config.dictConfig(_config.dict())


def create_logger(
    context_name: str,
    logger_name: Optional[str] = _config.LOGGER_NAME,
) -> Logger:
    """
    Retorna um objeto logger configurado com as configurações definidas por LogConfig.

    Args:
        context_name (str): O nome do contexto para o qual o logger será usado.
        logger_name (str, opcional): O nome do logger. Se não especificado, será usado o valor padrão do objeto LogConfig.

    Returns:
        Logger: Um objeto logger configurado com base nas configurações fornecidas por LogConfig.

    Examples:
        >>> logger = create_logger('meu_contexto')
        >>> logger.error('Mensagem de informação', {'key': value})

        >>> logger_file = create_logger('meu_contexto', 'file')  # Salva os logs no arquivo app.log'.
        >>> logger_file.info('Mensagem de informação para o logger de arquivo')

    """
    if logger_name not in _config.dict()['loggers']:
        raise ValueError('Logger name does not exists')
    logger = logging.getLogger(logger_name)
    logger.name = context_name
    return logger


def set_trace_id(trace_id: str) -> None:
    """Seta o trace_id caso precise usar um valor conhecido"""
    PyTelemetryContextVar.set_trace_id(trace_id)
