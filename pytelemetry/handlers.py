import logging

from pytelemetry.formaters import PyTelemetryFormatter


class PyTelemetryHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)
        self.formatter = PyTelemetryFormatter()
