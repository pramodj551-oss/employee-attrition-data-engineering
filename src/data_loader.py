"""
==========================================================
Data Loader Module
----------------------------------------------------------
Employee Attrition Data Engineering Project

Author : Pramod Prakash Jadhav
==========================================================
"""

from pathlib import Path

import pandas as pd

from src.config import RAW_DATA_PATH
from src.logger import logger


def load_data(file_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Load employee attrition dataset.

    Parameters
    ----------
    file_path : Path
        Path to the CSV dataset.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.

    Raises
    ------
    FileNotFoundError
        If dataset does not exist.

    ValueError
        If dataset is empty.
    """

    logger.info("Loading dataset...")

    try:

        if not file_path.exists():

            logger.error(f"Dataset not found: {file_path}")

            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        df = pd.read_csv(file_path)

        if df.empty:

            logger.error("Dataset is empty.")

            raise ValueError("Dataset is empty.")

        logger.info("Dataset loaded successfully.")

        logger.info(f"Rows    : {df.shape[0]}")

        logger.info(f"Columns : {df.shape[1]}")

        return df

    except Exception as error:

        logger.exception(f"Error while loading dataset: {error}")

        raise


def dataset_info(df: pd.DataFrame) -> None:
    """
    Display basic dataset information.
    """

    logger.info("=" * 60)

    logger.info("DATASET INFORMATION")

    logger.info("=" * 60)

    logger.info(f"Rows              : {df.shape[0]}")

    logger.info(f"Columns           : {df.shape[1]}")

    logger.info(f"Missing Values    : {df.isnull().sum().sum()}")

    logger.info(f"Duplicate Records : {df.duplicated().sum()}")

    logger.info(f"Memory Usage      : "
                f"{round(df.memory_usage(deep=True).sum()/1024**2,2)} MB")

    logger.info("=" * 60)


if __name__ == "__main__":

    dataframe = load_data()

    dataset_info(dataframe)

    print(dataframe.head())
