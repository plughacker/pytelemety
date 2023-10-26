from contextvars import ContextVar


class PyTelemetryContextVar:
    __context_trace_id = ContextVar('trace_id', default=None)
    __resource = {}

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
