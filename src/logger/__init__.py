import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# constants for log configuration
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5* 1024*1024   # 5 MB
BACKUP_COUNT = 3        # Number of backup log file to keep


# construct logfile path
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
    Configures logging with a rotating file handler and a console
    """
    # create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] %(name)s %(levelname)s %(message)s")

    # file handler with rotating rotation

    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # console  handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handler to the logger

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# configuring the logger

configure_logger()