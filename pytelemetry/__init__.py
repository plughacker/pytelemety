import logging.config
from logging import Logger

from pytelemetry.context import PyTelemetryContextVar
from pytelemetry.logger import LogConfig

_config = LogConfig()

logging.config.dictConfig(_config.dict())


def create_logger(
    context_name: str,
) -> Logger:
    """
    Retorna um objeto logger configurado com as configurações definidas por LogConfig.

    Args:
        context_name (str): O nome do contexto para o qual o logger será usado.

    Returns:
        Logger: Um objeto logger configurado com base nas configurações fornecidas por LogConfig.

    Examples:
        >>> logger = create_logger('meu_contexto')
        >>> logger.error('Mensagem de informação', {'key': value})

    """
    a = _config.get_logger_name()
    logger = logging.getLogger(a)
    logger.name = context_name
    return logger


def set_trace_id(trace_id: str) -> None:
    """Seta o trace_id caso precise usar um valor conhecido"""
    PyTelemetryContextVar.set_trace_id(trace_id)
