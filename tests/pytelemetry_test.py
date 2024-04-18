import os
import uuid
from unittest.mock import patch

import pytest

from pytelemetry import create_logger, set_trace_id
from pytelemetry.context import PyTelemetryContextVar


@pytest.mark.parametrize('save_to_file', [False, True])
@pytest.mark.parametrize('level', ['info', 'debug', 'error'])
def test_pytelemetry_logger(level: str, save_to_file: bool):
    if os.path.exists('app.log'):
        os.remove('app.log')
    with patch(
        'pytelemetry.logger.LogConfig.is_logger_to_file', return_value=save_to_file
    ), patch('pytelemetry.logger.LogConfig.LOG_LEVEL', return_value='DEBUG'):
        logger = create_logger('Pytest')
        try:
            getattr(logger, level)(f'Message by {level}')
            assert os.path.exists('app.log') == save_to_file
        except Exception as error:
            assert False, error


def test_pytelemetry_trace_id():
    trace_id = str(uuid.uuid4())
    set_trace_id(trace_id)
    assert trace_id == PyTelemetryContextVar.get_trace_id()
