import json
import logging
import time

from pytelemetry.context import PyTelemetryContextVar
from pytelemetry.utils.encoders import CustomEncoder


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
        log: dict = self.log_record_to_dict(record)
        try:
            return json.dumps(log, cls=CustomEncoder)
        except Exception:
            log['Attributes'] = []
            return json.dumps(log, cls=CustomEncoder)

    def get_trace_id(self):
        return PyTelemetryContextVar.get_trace_id()

    def log_record_to_dict(self, record: logging.LogRecord):
        return {
            '__unixNanoTime': int(time.time()),
            'Timestamp': int(time.time()),
            'TraceId': self.get_trace_id(),
            'SeverityText': record.levelname,
            'SeverityNumber': self.LEVELS[record.levelname.lower()]['number'],
            'Body': record.getMessage(),
            'Resource': PyTelemetryContextVar.get_resource(),
            'InstrumentationScope': record.name,
            'Attributes': record.args,
        }
