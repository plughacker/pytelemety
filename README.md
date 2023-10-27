# pytelemetry

A simple and default open telemetry log formatter

## Quick Start

* Install
```bash
pip install git+https://github.com/joaofilho-plug/pytelemetry.git@main
```

* Create an env var

```
LOGGER_NAME=your_project_name
```

* Import in your project

```python
from pytelemetry import get_logger

logger = get_logger() # returns default python logger

logger.error('division by zero')

```

Output
```json
{"Timestamp": 1698414960, "TraceId": "a0909332-03a7-4ff5-84b1-7373793042ce", "SeverityText": "ERROR", "SeverityNumber": 17, "Body": "division by zero", "Resource": {}, "InstrumentationScope": "your_project_name", "Attributes": []}
```


[Baseado em](https://github.com/diego-malga/pytelemetry)
