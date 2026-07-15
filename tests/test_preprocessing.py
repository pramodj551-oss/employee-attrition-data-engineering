import unittest

from src.data_loader import load_data
from src.preprocessing import DataPreprocessor


class TestPreprocessing(unittest.TestCase):

    def test_preprocessing(self):

        df = load_data()

        processor = DataPreprocessor(df)

        cleaned_df = processor.process()

        self.assertIsNotNone(cleaned_df)

        self.assertFalse(cleaned_df.empty)

        self.assertEqual(
            cleaned_df.duplicated().sum(),
            0
        )


if __name__ == "__main__":

    unittest.main()
