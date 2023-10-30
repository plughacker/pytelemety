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
            '__unixNanoTime': current_timestamp,
            'Timestamp': current_timestamp,
            'TraceId': trace_id,
            'SeverityText': 'ERROR',
            'SeverityNumber': 17,
            'Body': 'Test error message',
            'Resource': {
                'service_name': 'service_not_named',
                'service_version': '0.0.1',
                'service_environment': None,
            },
            'InstrumentationScope': 'Pytest',
            'Attributes': {'param1': 'value1', 'param2': 'value2'},
        }
    )
