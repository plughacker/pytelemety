import os
import uuid

import pytest

from pytelemetry import create_logger, set_trace_id
from pytelemetry.context import PyTelemetryContextVar


@pytest.mark.parametrize('save_to_file', [False, True])
@pytest.mark.parametrize('level', ['info', 'debug', 'error'])
def test_pytelemetry_logger(level: str, save_to_file: bool):
    if os.path.exists('app.log'):
        os.remove('app.log')

    logger = create_logger('Pytest', save_to_file=save_to_file)
    try:
        getattr(logger, level)(f'Message by {level}')
    except Exception as error:
        assert False, error
    assert os.path.exists('app.log') == save_to_file


def test_pytelemetry_trace_id():
    trace_id = str(uuid.uuid4())
    set_trace_id(trace_id)
    assert trace_id == PyTelemetryContextVar.get_trace_id()
