import unittest

from src.data_loader import load_data


class TestDataLoader(unittest.TestCase):

    def test_load_dataset(self):

        df = load_data()

        self.assertIsNotNone(df)

        self.assertFalse(df.empty)

        self.assertGreater(df.shape[0], 0)

        self.assertGreater(df.shape[1], 0)


if __name__ == "__main__":

    unittest.main()
