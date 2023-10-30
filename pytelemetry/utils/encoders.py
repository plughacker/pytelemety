import json
from datetime import date, datetime
from uuid import UUID


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        if isinstance(obj, Exception):
            return str(obj)
        if callable(obj):
            return obj.__name__
        if hasattr(obj, '__class__'):
            return obj.__class__.__name__
        try:
            return json.JSONEncoder.default(self, obj)
        except Exception:
            return str(obj)
