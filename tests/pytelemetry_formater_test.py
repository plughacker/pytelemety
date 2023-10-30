import json
import logging
from unittest.mock import MagicMock, patch

from pytelemetry.formaters import PyTelemetryFormatter


@patch('time.time')
@patch('pytelemetry.formaters.PyTelemetryFormatter.get_trace_id')
def test_pytelemetry_formatter_log_level_error(
    mock_trace_id: MagicMock,
    mock_time: MagicMock,
    trace_id: str,
    current_timestamp: int,
    expected_output_error: dict,
):
    mock_trace_id.return_value = trace_id
    mock_time.return_value = current_timestamp

    formatter = PyTelemetryFormatter()
    record = logging.makeLogRecord(
        {
            'name': 'Pytest',
            'levelname': 'ERROR',
            'msg': 'Test error message',
            'args': {'param1': 'value1', 'param2': 'value2'},
        }
    )
    formatted_output = formatter.format(record)
    assert formatted_output == expected_output_error


@patch('time.time')
@patch('pytelemetry.formaters.PyTelemetryFormatter.get_trace_id')
def test_pytelemetry_formatter_with_invalid_arg(
    mock_trace_id: MagicMock,
    mock_time: MagicMock,
    trace_id: str,
    current_timestamp: int,
):
    mock_trace_id.return_value = trace_id
    mock_time.return_value = current_timestamp

    formatter = PyTelemetryFormatter()
    record = logging.makeLogRecord(
        {
            'name': 'Pytest',
            'levelname': 'ERROR',
            'msg': 'Test error message',
            'args': {Exception: Exception},
        }
    )
    formatted_output = formatter.format(record)
    assert json.loads(formatted_output)['Attributes'] == []
