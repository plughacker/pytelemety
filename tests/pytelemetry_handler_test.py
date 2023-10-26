import logging
from io import StringIO

from pytelemetry.handlers import PyTelemetryHandler


def test_pytelemetry_handler():
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)

    stream = StringIO()
    handler = PyTelemetryHandler(stream)

    logger.addHandler(handler)

    logger.debug('Debug message')
    logger.info('Info message')

    log_output = stream.getvalue()

    assert 'Debug message' in log_output
    assert 'Info message' in log_output
