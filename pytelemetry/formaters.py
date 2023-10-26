import json
import logging
import time
import uuid

from pytelemetry.context import PyTelemetryContextVar


class PyTelemetryFormatter(logging.Formatter):
    LEVELS = {
        'trace': {
            'text': 'TRACE',
            'number': 1,
        },
        'debug': {
            'text': 'DEBUG',
            'number': 5,
        },
        'info': {
            'text': 'INFO',
            'number': 9,
        },
        'warning': {
            'text': 'WARN',
            'number': 13,
        },
        'error': {
            'text': 'ERROR',
            'number': 17,
        },
        'critical': {
            'text': 'FATAL',
            'number': 21,
        },
    }

    def format(self, record: logging.LogRecord):
        log_dict = self.log_record_to_dict(record)
        return json.dumps(log_dict)

    def get_trace_id(self):
        trace_id = PyTelemetryContextVar.get_trace_id()

        if trace_id is None:
            trace_id = str(uuid.uuid4())
            PyTelemetryContextVar.set_trace_id(trace_id)
        return trace_id

    def log_record_to_dict(self, record: logging.LogRecord):
        return {
            'timestamp': int(time.time()),
            'trace_id': self.get_trace_id(),
            'severity_text': record.levelname,
            'severity_number': self.LEVELS[record.levelname.lower()]['number'],
            'message': record.getMessage(),
            'resource': PyTelemetryContextVar.get_resource(),
            'scope': record.name,
            'attributes': record.args,
        }
