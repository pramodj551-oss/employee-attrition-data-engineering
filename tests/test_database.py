import unittest

from src.data_loader import load_data
from src.preprocessing import DataPreprocessor
from src.database import DatabaseManager


class TestDatabase(unittest.TestCase):

    def test_database_creation(self):

        df = load_data()

        processor = DataPreprocessor(df)

        cleaned_df = processor.process()

        db = DatabaseManager()

        db.create_database(cleaned_df)

        result = db.record_count()

        self.assertGreater(
            int(result.iloc[0]["Total_Records"]),
            0
        )


if __name__ == "__main__":

    unittest.main()
