# pytelemetry

A simple and default open telemetry log formatter

## Quick Start

* Install
```bash
pip install git+https://github.com/plughacker/pytelemety.git@v0.0.1
```

* Create an env var

```
SERVICE_NAME=your_project_name
SERVICE_VERSION=0.0.1
SERVICE_ENVIRONMENT=dev | prod | None
LOGGER_SAVE_TO_FILE=True | False # When True salve logs in app.log file
```

* Import in your project

```python
from pytelemetry import create_logger

logger = create_logger('My Controller') # returns default python logger

logger.error('division by zero')

```

Output
```json
{"Timestamp": 1698414960, "TraceId": "a0909332-03a7-4ff5-84b1-7373793042ce", "SeverityText": "ERROR", "SeverityNumber": 17, "Body": "division by zero", "Resource": {"service_name": "service_not_named", "service_version": "0.0.1", "service_environment": null}, "InstrumentationScope": "Class or mehtod name", "Attributes": []}
```


[Baseado em](https://github.com/diego-malga/pytelemetry)
