"""
==========================================================
Configuration Module
----------------------------------------------------------
Employee Attrition Data Engineering Project

Author : Pramod Prakash Jadhav
==========================================================
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# ----------------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------------
load_dotenv()

# ----------------------------------------------------------
# Project Information
# ----------------------------------------------------------
PROJECT_NAME = "Employee Attrition Data Engineering"

PROJECT_VERSION = "1.0.0"

AUTHOR = "Pramod Prakash Jadhav"

# ----------------------------------------------------------
# Project Root Directory
# ----------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------
# Data Directories
# ----------------------------------------------------------
DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

DATABASE_DIR = DATA_DIR / "database"

# ----------------------------------------------------------
# Output Directories
# ----------------------------------------------------------
OUTPUT_DIR = PROJECT_ROOT / "outputs"

CHARTS_DIR = OUTPUT_DIR / "charts"

REPORTS_DIR = OUTPUT_DIR / "reports"

LOGS_DIR = OUTPUT_DIR / "logs"

# ----------------------------------------------------------
# Notebook Directory
# ----------------------------------------------------------
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"

# ----------------------------------------------------------
# SQL Directory
# ----------------------------------------------------------
SQL_DIR = PROJECT_ROOT / "sql"

# ----------------------------------------------------------
# Tests Directory
# ----------------------------------------------------------
TEST_DIR = PROJECT_ROOT / "tests"

# ----------------------------------------------------------
# Dataset File
# ----------------------------------------------------------
RAW_DATA_PATH = Path(
    os.getenv(
        "RAW_DATA_PATH",
        RAW_DATA_DIR / "employee_attrition.csv"
    )
)

PROCESSED_DATA_PATH = Path(
    os.getenv(
        "PROCESSED_DATA_PATH",
        PROCESSED_DATA_DIR / "cleaned_employee_attrition.csv"
    )
)

# ----------------------------------------------------------
# SQLite Database
# ----------------------------------------------------------
DATABASE_PATH = Path(
    os.getenv(
        "DATABASE_PATH",
        DATABASE_DIR / "employee_attrition.db"
    )
)

# ----------------------------------------------------------
# Logging
# ----------------------------------------------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ----------------------------------------------------------
# Application Settings
# ----------------------------------------------------------
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

SAVE_CHARTS = os.getenv(
    "SAVE_CHARTS",
    "True"
).lower() == "true"

SAVE_REPORTS = os.getenv(
    "SAVE_REPORTS",
    "True"
).lower() == "true"

# ----------------------------------------------------------
# Create Required Directories
# ----------------------------------------------------------
DIRECTORIES = [

    DATA_DIR,

    RAW_DATA_DIR,

    PROCESSED_DATA_DIR,

    DATABASE_DIR,

    OUTPUT_DIR,

    CHARTS_DIR,

    REPORTS_DIR,

    LOGS_DIR,

    NOTEBOOK_DIR,

    SQL_DIR,

    TEST_DIR

]

for directory in DIRECTORIES:
    directory.mkdir(
        parents=True,
        exist_ok=True
    )

# ----------------------------------------------------------
# Display Configuration (Optional)
# ----------------------------------------------------------
def show_config():
    """
    Print important project configuration.
    """

    print("=" * 60)
    print(PROJECT_NAME)
    print("=" * 60)

    print(f"Version           : {PROJECT_VERSION}")
    print(f"Project Root      : {PROJECT_ROOT}")
    print(f"Raw Dataset       : {RAW_DATA_PATH}")
    print(f"Processed Dataset : {PROCESSED_DATA_PATH}")
    print(f"Database          : {DATABASE_PATH}")
    print(f"Charts Folder     : {CHARTS_DIR}")
    print(f"Reports Folder    : {REPORTS_DIR}")
    print(f"Logs Folder       : {LOGS_DIR}")
    print(f"Debug Mode        : {DEBUG}")
    print(f"Save Charts       : {SAVE_CHARTS}")
    print(f"Save Reports      : {SAVE_REPORTS}")
    print("=" * 60)


if __name__ == "__main__":
    show_config()
