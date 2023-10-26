import pytest

from pytelemetry import get_logger


@pytest.mark.parametrize('level', ['info', 'debug', 'error'])
def test_pytelemetry_logger(level: str):
    message = f'Message by {level}'
    logger = get_logger()
    try:
        getattr(logger, level)(message)
    except Exception as error:
        assert False, error
