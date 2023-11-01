from decouple import config


class LogConfig:
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = config('LOGGER_NAME', default='pytelemetry')
    LOG_FORMAT: str = '%(levelprefix)s | %(asctime)s | %(message)s'
    LOG_LEVEL: str = 'DEBUG'

    # Logging config
    version = 1
    disable_existing_loggers = False

    formatters = {
        'pytelemetry_formatter': {
            '()': 'pytelemetry.formaters.PyTelemetryFormatter',
            'fmt': LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    }
    filters = {
        'sensitive_data_filter': {'()': 'pytelemetry.filters.SensitiveDataFilter'}
    }
    handlers = {
        'pytelemetry_handler': {
            'class': 'pytelemetry.handlers.PyTelemetryHandler',
            'formatter': 'pytelemetry_formatter',
            'stream': 'ext://sys.stdout',
            'filters': ['sensitive_data_filter'],
        },
        'pytelemetry_file_handler': {
            'class': 'pytelemetry.handlers.PyTelemetryFileWriteHandler',
            'formatter': 'pytelemetry_formatter',
            'stream': 'ext://sys.stdout',
            'filters': ['sensitive_data_filter'],
        },
    }

    @property
    def FILE_LOGGER_NAME(self):
        return f'{self.LOGGER_NAME}_file'

    def dict(self):
        return {
            'LOGGER_NAME': self.LOGGER_NAME,
            'LOG_FORMAT': self.LOG_FORMAT,
            'LOG_LEVEL': self.LOG_LEVEL,
            'version': self.version,
            'disable_existing_loggers': self.disable_existing_loggers,
            'formatters': self.formatters,
            'filters': self.filters,
            'handlers': self.handlers,
            'loggers': {
                self.LOGGER_NAME: {
                    'handlers': ['pytelemetry_handler'],
                    'level': self.LOG_LEVEL,
                    'propagate': False,
                },
                self.FILE_LOGGER_NAME: {
                    'handlers': ['pytelemetry_file_handler'],
                    'level': self.LOG_LEVEL,
                    'propagate': False,
                },
            },
        }
