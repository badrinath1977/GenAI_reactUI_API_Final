import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logging/logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        f"{LOG_DIR}/application.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    error_handler = RotatingFileHandler(
        f"{LOG_DIR}/error.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(error_handler)

    return logger
