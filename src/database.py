"""
==========================================================
Database Module
----------------------------------------------------------
Employee Attrition Data Engineering Project

Author : Pramod Prakash Jadhav
==========================================================

Description
-----------
This module manages SQLite database operations:
- Create database connection
- Create employee table
- Insert processed dataset
- Execute SQL queries
- Fetch query results
- Close database connection
"""

import sqlite3
from typing import Optional

import pandas as pd

from src.config import DATABASE_PATH
from src.logger import logger


class DatabaseManager:
    """
    SQLite Database Manager.
    """

    def __init__(self, db_path=DATABASE_PATH):

        self.db_path = db_path

        self.connection: Optional[sqlite3.Connection] = None

    # ---------------------------------------------------------
    # Connect Database
    # ---------------------------------------------------------
    def connect(self):

        try:

            self.connection = sqlite3.connect(self.db_path)

            logger.info(
                f"Connected to SQLite Database: {self.db_path}"
            )

        except sqlite3.Error as error:

            logger.exception(error)

            raise

    # ---------------------------------------------------------
    # Close Connection
    # ---------------------------------------------------------
    def close(self):

        if self.connection:

            self.connection.close()

            logger.info("Database connection closed.")

    # ---------------------------------------------------------
    # Store DataFrame
    # ---------------------------------------------------------
    def create_database(
        self,
        dataframe: pd.DataFrame,
        table_name="employee_attrition"
    ):

        try:

            self.connect()

            dataframe.to_sql(
                table_name,
                self.connection,
                if_exists="replace",
                index=False
            )

            logger.info(
                f"Table '{table_name}' created successfully."
            )

            logger.info(
                f"Inserted {len(dataframe)} rows."
            )

        except Exception as error:

            logger.exception(error)

            raise

        finally:

            self.close()

    # ---------------------------------------------------------
    # Execute SQL Query
    # ---------------------------------------------------------
    def execute_query(self, query):

        try:

            self.connect()

            cursor = self.connection.cursor()

            cursor.execute(query)

            self.connection.commit()

            logger.info("Query executed successfully.")

        except Exception as error:

            logger.exception(error)

            raise

        finally:

            self.close()

    # ---------------------------------------------------------
    # Fetch Query Results
    # ---------------------------------------------------------
    def fetch_query(self, query):

        try:

            self.connect()

            dataframe = pd.read_sql_query(
                query,
                self.connection
            )

            logger.info(
                "Query results fetched successfully."
            )

            return dataframe

        except Exception as error:

            logger.exception(error)

            raise

        finally:

            self.close()

    # ---------------------------------------------------------
    # Show Tables
    # ---------------------------------------------------------
    def show_tables(self):

        query = """
        SELECT name
        FROM sqlite_master
        WHERE type='table';
        """

        return self.fetch_query(query)

    # ---------------------------------------------------------
    # Table Information
    # ---------------------------------------------------------
    def table_info(
        self,
        table_name="employee_attrition"
    ):

        query = f"""
        PRAGMA table_info({table_name});
        """

        return self.fetch_query(query)

    # ---------------------------------------------------------
    # Count Records
    # ---------------------------------------------------------
    def record_count(
        self,
        table_name="employee_attrition"
    ):

        query = f"""
        SELECT COUNT(*) AS Total_Records
        FROM {table_name};
        """

        return self.fetch_query(query)

    # ---------------------------------------------------------
    # Preview Table
    # ---------------------------------------------------------
    def preview_table(
        self,
        table_name="employee_attrition",
        limit=5
    ):

        query = f"""
        SELECT *
        FROM {table_name}
        LIMIT {limit};
        """

        return self.fetch_query(query)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------
if __name__ == "__main__":

    from src.data_loader import load_data
    from src.preprocessing import DataPreprocessor

    logger.info("=" * 60)

    logger.info("Database Module Testing")

    logger.info("=" * 60)

    df = load_data()

    df = DataPreprocessor(df).process()

    db = DatabaseManager()

    db.create_database(df)

    print("\nTables")

    print(db.show_tables())

    print("\nRecord Count")

    print(db.record_count())

    print("\nTable Preview")

    print(db.preview_table())
