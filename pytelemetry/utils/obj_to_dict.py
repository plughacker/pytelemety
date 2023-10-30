import re
import uuid


def obj_to_dict(obj, visited=None):
    if visited is None:
        visited = set()
    if id(obj) in visited:
        return None

    visited.add(id(obj))
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if isinstance(obj, (list, tuple)):
        return [obj_to_dict(item, visited) for item in obj]
    if isinstance(obj, dict):
        return {str(key): obj_to_dict(value, visited) for key, value in obj.items()}
    if hasattr(obj, '__dict__'):
        return {
            str(key): obj_to_dict(value, visited) for key, value in obj.__dict__.items()
        }
    if isinstance(obj, re.Pattern):
        return f'{obj.pattern}'
    return str(obj)
