import logging.config
from logging import Logger

from pytelemetry.context import PyTelemetryContextVar
from pytelemetry.logger import LogConfig

_config = LogConfig()

logging.config.dictConfig(_config.dict())


def create_logger(
    context_name: str,
    save_to_file: bool = False,
) -> Logger:
    """
    Retorna um objeto logger configurado com as configurações definidas por LogConfig.

    Args:
        context_name (str): O nome do contexto para o qual o logger será usado.
        save_to_file (bool, opcional): Se True, os logs serão salvos no arquivo app.log.

    Returns:
        Logger: Um objeto logger configurado com base nas configurações fornecidas por LogConfig.

    Examples:
        >>> logger = create_logger('meu_contexto')
        >>> logger.error('Mensagem de informação', {'key': value})

        >>> logger_file = create_logger('meu_contexto', 'file')  # Salva os logs no arquivo app.log'.
        >>> logger_file.info('Mensagem de informação para o logger de arquivo')

    """
    logger = logging.getLogger(
        _config.FILE_LOGGER_NAME if save_to_file else _config.LOGGER_NAME
    )
    logger.name = context_name
    return logger


def set_trace_id(trace_id: str) -> None:
    """Seta o trace_id caso precise usar um valor conhecido"""
    PyTelemetryContextVar.set_trace_id(trace_id)
