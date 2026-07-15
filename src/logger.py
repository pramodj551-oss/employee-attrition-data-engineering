"""
==========================================================
Logger Module
----------------------------------------------------------
Employee Attrition Data Engineering Project

Author : Pramod Prakash Jadhav
==========================================================
"""

import logging
from logging import Logger

from src.config import LOG_LEVEL
from src.config import LOGS_DIR

# ----------------------------------------------------------
# Log File Path
# ----------------------------------------------------------
LOG_FILE = LOGS_DIR / "employee_attrition.log"

# ----------------------------------------------------------
# Logger Configuration
# ----------------------------------------------------------
logger: Logger = logging.getLogger("EmployeeAttrition")

logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

# Prevent duplicate log messages
logger.propagate = False

# ----------------------------------------------------------
# Formatter
# ----------------------------------------------------------
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ----------------------------------------------------------
# Add Handlers Only Once
# ----------------------------------------------------------
if not logger.handlers:

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(
        LOG_FILE,
        mode="a",
        encoding="utf-8"
    )

    file_handler.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# ----------------------------------------------------------
# Test Logger
# ----------------------------------------------------------
if __name__ == "__main__":

    logger.info("Logger initialized successfully.")

    logger.warning("Sample warning message.")

    logger.error("Sample error message.")
