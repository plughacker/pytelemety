# pytelemetry

A simple and default open telemetry log formatter

## how to use

* Install
```bash
    pip install git+https://github.com/joaofilho-plug/pytelemetry.git@main
```

* Create an env var

```
LOGGER_NAME=your_project_name
```


```python
from pytelemetry import get_logger

logger = get_logger() # returns default python logger

logger.error('division by zero')

```

Output
```json
{"timestamp": 1698356223, "trace_id": "0d5e33c8-8010-43d0-87ee-93f856f1c860", "severity_text": "ERROR", "severity_number": 17, "message": "division by zero", "resource": {}, "scope": "your_project_name", "attributes": []}
```
