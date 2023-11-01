import logging
from logging import LogRecord

from pytelemetry.formaters import PyTelemetryFormatter


class PyTelemetryHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)
        self.formatter = PyTelemetryFormatter()


class PyTelemetryFileWriteHandler(PyTelemetryHandler):
    def format(self, record: LogRecord) -> str:
        output = super().format(record)
        with open('app.log', 'a') as file:
            file.write(output + '\n')
        return output
