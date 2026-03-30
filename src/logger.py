import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def get_logger(name: str):
    """
    Create and configure a logger with both console and file handlers.
    """

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "cleaner.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if logger is called multiple times
    if logger.handlers:
        return logger
    
    # Console handler (INFO and above)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter("[%(levelname)s] %(message)s")
    console_handler.setFormatter(console_format)

    # File handler (DEBUG and above)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=500_000, backupCount=3
    )

    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger