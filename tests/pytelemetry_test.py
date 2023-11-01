import uuid

import pytest

from pytelemetry import create_logger, set_trace_id
from pytelemetry.context import PyTelemetryContextVar


@pytest.mark.parametrize('level', ['info', 'debug', 'error'])
def test_pytelemetry_logger(level: str):
    message = f'Message by {level}'
    logger = create_logger('Pytest')
    try:
        getattr(logger, level)(message)
    except Exception as error:
        assert False, error


@pytest.mark.parametrize('logger_name', ['invalid_name', None, 1])
def test_pytelemetry_logger_not_fount(logger_name):
    with pytest.raises(ValueError):
        create_logger('Pytest', logger_name)


def test_pytelemetry_trace_id():
    trace_id = str(uuid.uuid4())
    set_trace_id(trace_id)
    assert trace_id == PyTelemetryContextVar.get_trace_id()
