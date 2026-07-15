"""
==========================================================
Utility Functions Module
----------------------------------------------------------
Employee Attrition Data Engineering Project

Author : Pramod Prakash Jadhav
==========================================================
"""

from typing import Dict, List

import pandas as pd

from src.logger import logger


def dataset_summary(df: pd.DataFrame) -> Dict[str, object]:
    """
    Generate dataset summary.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    dict
    """

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Records": int(df.duplicated().sum()),
        "Memory Usage (MB)": round(
            df.memory_usage(deep=True).sum() / (1024 ** 2),
            2
        ),
    }

    return summary


def print_dataset_summary(df: pd.DataFrame) -> None:
    """
    Print dataset summary in a readable format.
    """

    summary = dataset_summary(df)

    logger.info("=" * 60)
    logger.info("DATASET SUMMARY")
    logger.info("=" * 60)

    for key, value in summary.items():
        logger.info(f"{key:<22}: {value}")

    logger.info("=" * 60)


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return missing value report.
    """

    report = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values,
        "Percentage": (
            df.isnull().sum() / len(df) * 100
        ).round(2).values
    })

    return report.sort_values(
        by="Missing Values",
        ascending=False
    )


def duplicate_report(df: pd.DataFrame) -> int:
    """
    Return duplicate record count.
    """

    return int(df.duplicated().sum())


def numerical_columns(df: pd.DataFrame) -> List[str]:
    """
    Return numerical columns.
    """

    return list(
        df.select_dtypes(
            include=["number"]
        ).columns
    )


def categorical_columns(df: pd.DataFrame) -> List[str]:
    """
    Return categorical columns.
    """

    return list(
        df.select_dtypes(
            include=["object", "category"]
        ).columns
    )


def memory_usage(df: pd.DataFrame) -> float:
    """
    Return dataframe memory usage in MB.
    """

    return round(
        df.memory_usage(deep=True).sum() / (1024 ** 2),
        2
    )


def unique_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return unique values for each column.
    """

    report = pd.DataFrame({
        "Column": df.columns,
        "Unique Values": [
            df[col].nunique()
            for col in df.columns
        ]
    })

    return report


def save_dataframe(
    df: pd.DataFrame,
    output_path: str
) -> None:
    """
    Save dataframe as CSV.
    """

    df.to_csv(
        output_path,
        index=False
    )

    logger.info(
        f"Data saved successfully -> {output_path}"
    )


if __name__ == "__main__":

    from src.data_loader import load_data

    dataframe = load_data()

    print_dataset_summary(dataframe)

    print("\nMissing Value Report")
    print(missing_value_report(dataframe))

    print("\nDuplicate Records")
    print(duplicate_report(dataframe))

    print("\nNumerical Columns")
    print(numerical_columns(dataframe))

    print("\nCategorical Columns")
    print(categorical_columns(dataframe))

    print("\nMemory Usage (MB)")
    print(memory_usage(dataframe))

    print("\nUnique Value Report")
    print(unique_value_report(dataframe).head())
