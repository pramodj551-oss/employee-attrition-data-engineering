"""
==========================================================
Employee Attrition Data Engineering Project
----------------------------------------------------------
Author : Pramod Prakash Jadhav
Project: End-to-End Applied AI & ML Data Product
Part   : 1 - Data Engineering
==========================================================
"""

from src.logger import logger
from src.data_loader import load_data
from src.preprocessing import DataPreprocessor
from src.feature_engineering import FeatureEngineering
from src.database import DatabaseManager
from src.eda import EDA


def main():
    """
    Main pipeline for the Employee Attrition
    Data Engineering Project.
    """

    try:

        logger.info("=" * 60)
        logger.info("Employee Attrition Data Engineering Started")
        logger.info("=" * 60)

        # -------------------------------------------------
        # Step 1 : Load Dataset
        # -------------------------------------------------
        logger.info("Step 1 : Loading Dataset")

        df = load_data()

        logger.info(f"Dataset Shape : {df.shape}")

        # -------------------------------------------------
        # Step 2 : Data Cleaning
        # -------------------------------------------------
        logger.info("Step 2 : Data Preprocessing")

        processor = DataPreprocessor(df)

        cleaned_df = processor.process()

        logger.info("Data Cleaning Completed")

        # -------------------------------------------------
        # Step 3 : Feature Engineering
        # -------------------------------------------------
        logger.info("Step 3 : Feature Engineering")

        engineer = FeatureEngineering(cleaned_df)

        feature_df = engineer.process()

        logger.info("Feature Engineering Completed")

        # -------------------------------------------------
        # Step 4 : SQLite Database
        # -------------------------------------------------
        logger.info("Step 4 : Database Creation")

        db = DatabaseManager()

        db.create_database(feature_df)

        logger.info("Database Created Successfully")

        # -------------------------------------------------
        # Step 5 : Exploratory Data Analysis
        # -------------------------------------------------
        logger.info("Step 5 : Running EDA")

        analysis = EDA(feature_df)

        analysis.run()

        logger.info("EDA Completed")

        logger.info("=" * 60)
        logger.info("Project Executed Successfully")
        logger.info("=" * 60)

    except Exception as error:

        logger.exception(f"Pipeline Failed : {error}")


if __name__ == "__main__":
    main()
