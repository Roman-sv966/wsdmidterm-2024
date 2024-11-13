import logging
import logging.config
import os

def configure_logging(custom_log_level=None):
    """
    Set up logging for the application with dynamic options for log level and file path.
    If no log level is specified, it defaults to INFO.
    """
    # Ensure the logs directory is created
    os.makedirs("logs", exist_ok=True)

    # Set default log level and log file if not provided in environment or parameters
    log_level = (custom_log_level or os.getenv("LOG_LEVEL", "INFO")).upper()
    log_file_path = os.getenv("LOG_FILE_PATH", "logs/application.log")
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Define logging configuration dictionary
    logging_configuration = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": log_format
            }
        },
        "handlers": {
            "console_handler": {
                "class": "logging.StreamHandler",
                "level": log_level,
                "formatter": "default",
                "stream": "ext://sys.stdout"
            },
            "file_handler": {
                "class": "logging.FileHandler",
                "level": log_level,
                "formatter": "default",
                "filename": log_file_path,
                "mode": "a"
            }
        },
        "root": {
            "level": log_level,
            "handlers": ["console_handler", "file_handler"]
        }
    }

    # Configure logging using the configuration dictionary
    logging.config.dictConfig(logging_configuration)
    logging.info("Logging is set up. Level: %s, File: %s", log_level, log_file_path)
