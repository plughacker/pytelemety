import json

import pytest


@pytest.fixture
def current_timestamp():
    return 1635237638


@pytest.fixture
def trace_id():
    return 'b5fb3461-2206-428b-ac3b-e4e8ab00d2fd'


@pytest.fixture
def expected_output_error(current_timestamp, trace_id):
    return json.dumps(
        {
            'timestamp': current_timestamp,
            'trace_id': trace_id,
            'severity_text': 'ERROR',
            'severity_number': 17,
            'message': 'Test error message',
            'resource': {},
            'scope': 'test_logger',
            'attributes': {'param1': 'value1', 'param2': 'value2'},
        }
    )
