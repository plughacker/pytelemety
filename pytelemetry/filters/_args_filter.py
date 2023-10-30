import logging

from pytelemetry.utils.obj_to_dict import obj_to_dict


class ArgsFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        record.args = obj_to_dict(record.args)
        return record
