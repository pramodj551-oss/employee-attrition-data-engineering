"""
==========================================================
Data Preprocessing Module
----------------------------------------------------------
Employee Attrition Data Engineering Project

Author : Pramod Prakash Jadhav
==========================================================
"""

from typing import Optional

import pandas as pd

from src.config import PROCESSED_DATA_PATH
from src.logger import logger


class DataPreprocessor:
    """
    Production-ready data preprocessing pipeline.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def remove_duplicates(self) -> None:
        """
        Remove duplicate records.
        """

        before = len(self.df)

        self.df.drop_duplicates(inplace=True)

        after = len(self.df)

        logger.info(
            f"Duplicate Records Removed : {before - after}"
        )

    def handle_missing_values(self) -> None:
        """
        Handle missing values using:
        - Median for numerical columns
        - Mode for categorical columns
        """

        missing = self.df.isnull().sum().sum()

        logger.info(
            f"Missing Values Found : {missing}"
        )

        if missing == 0:

            logger.info("No missing values detected.")

            return

        numeric_columns = self.df.select_dtypes(
            include=["number"]
        ).columns

        categorical_columns = self.df.select_dtypes(
            include=["object", "category"]
        ).columns

        self.df[numeric_columns] = self.df[
            numeric_columns
        ].fillna(
            self.df[numeric_columns].median()
        )

        for column in categorical_columns:

            mode = self.df[column].mode()[0]

            self.df[column] = self.df[column].fillna(
                mode
            )

        logger.info("Missing values handled successfully.")

    def validate_data_types(self) -> None:
        """
        Display dataset data types.
        """

        logger.info("Validating data types...")

        for column, dtype in self.df.dtypes.items():

            logger.info(f"{column:<30} {dtype}")

    def remove_negative_values(self) -> None:
        """
        Remove negative values from numeric columns.
        """

        numeric_columns = self.df.select_dtypes(
            include=["number"]
        ).columns

        for column in numeric_columns:

            negative_count = (self.df[column] < 0).sum()

            if negative_count > 0:

                logger.warning(
                    f"{column}: {negative_count} negative values found."
                )

                self.df = self.df[
                    self.df[column] >= 0
                ]

        logger.info("Negative value validation completed.")

    def detect_outliers(self) -> None:
        """
        Detect outliers using IQR method.
        """

        numeric_columns = self.df.select_dtypes(
            include=["number"]
        ).columns

        logger.info("Running outlier detection...")

        for column in numeric_columns:

            q1 = self.df[column].quantile(0.25)

            q3 = self.df[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr

            upper = q3 + 1.5 * iqr

            outliers = (
                (self.df[column] < lower)
                |
                (self.df[column] > upper)
            ).sum()

            logger.info(
                f"{column:<30} Outliers : {outliers}"
            )

    def validate_dataset(self) -> None:
        """
        Validate final dataset.
        """

        logger.info("=" * 60)

        logger.info("FINAL DATASET VALIDATION")

        logger.info("=" * 60)

        logger.info(f"Rows : {self.df.shape[0]}")

        logger.info(f"Columns : {self.df.shape[1]}")

        logger.info(
            f"Missing Values : {self.df.isnull().sum().sum()}"
        )

        logger.info(
            f"Duplicate Records : {self.df.duplicated().sum()}"
        )

        logger.info("=" * 60)

    def save_processed_data(
        self,
        output_path: Optional[str] = None
    ) -> None:
        """
        Save processed dataset.
        """

        path = output_path or PROCESSED_DATA_PATH

        self.df.to_csv(
            path,
            index=False
        )

        logger.info(
            f"Processed dataset saved at : {path}"
        )

    def process(self) -> pd.DataFrame:
        """
        Execute preprocessing pipeline.
        """

        logger.info("=" * 60)

        logger.info("STARTING DATA PREPROCESSING")

        logger.info("=" * 60)

        self.remove_duplicates()

        self.handle_missing_values()

        self.validate_data_types()

        self.remove_negative_values()

        self.detect_outliers()

        self.validate_dataset()

        self.save_processed_data()

        logger.info("=" * 60)

        logger.info("DATA PREPROCESSING COMPLETED")

        logger.info("=" * 60)

        return self.df


if __name__ == "__main__":

    from src.data_loader import load_data

    dataframe = load_data()

    processor = DataPreprocessor(dataframe)

    cleaned_dataframe = processor.process()

    print(cleaned_dataframe.head())
