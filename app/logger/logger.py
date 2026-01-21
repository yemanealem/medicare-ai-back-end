import logging
from logging.handlers import RotatingFileHandler
import sys
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("medicare_ai_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(
    "logs/medicare_ai.log",
    maxBytes=10*1024*1024,
    backupCount=5
)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
