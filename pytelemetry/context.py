from contextvars import ContextVar
from uuid import uuid4

from decouple import config


class PyTelemetryContextVar:
    __context_trace_id = ContextVar('TraceId', default=str(uuid4()))
    __resource = {
        'service_name': config(
            'service_name', config('SERVICE_NAME', default='service_not_named')
        ),
        'service_version': config(
            'service_version', config('SERVICE_VERSION', default='0.0.1')
        ),
        'service_environment': config(
            'service_environment', config('SERVICE_ENVIRONMENT', default=None)
        ),
    }

    @staticmethod
    def set_resource(service_name, service_version, service_environment):
        PyTelemetryContextVar.__resource['service_name'] = service_name
        PyTelemetryContextVar.__resource['service_version'] = service_version
        PyTelemetryContextVar.__resource['service_environment'] = service_environment

    @staticmethod
    def get_resource():
        return PyTelemetryContextVar.__resource

    @staticmethod
    def set_trace_id(trace_id):
        PyTelemetryContextVar.__context_trace_id.set(trace_id)

    @staticmethod
    def get_trace_id():
        return PyTelemetryContextVar.__context_trace_id.get()
