import pandas as pd
import numpy as np
import unittest


# Method to create a DataFrame with missing values
def create_dataframe_with_missing_values():
    data = {
        'Column1': [1, np.nan, 3, 4, 5],
        'Column2': ['A', 'B', np.nan, 'D', 'E'],
        'Column3': [np.nan, 2.5, 3.5, np.nan, 5.5]
    }
    return pd.DataFrame(data)


# Method to identify missing values
def identify_missing_values(df):
    return df.isnull()


# Method to fill missing values
def fill_missing_values(df, fill_value):
    return df.fillna(fill_value)


# Method to drop rows with missing values
def drop_missing_values(df):
    return df.dropna()


# Unit Tests
class TestHandleMissingDataMethods(unittest.TestCase):

    def test_create_dataframe_with_missing_values(self):
        df = create_dataframe_with_missing_values()
        self.assertTrue(df.isnull().values.any())

    def test_identify_missing_values(self):
        df = create_dataframe_with_missing_values()
        missing_values = identify_missing_values(df)
        self.assertEqual(missing_values.shape, df.shape)

    def test_fill_missing_values(self):
        df = create_dataframe_with_missing_values()
        filled_df = fill_missing_values(df, 0)
        self.assertFalse(filled_df.isnull().values.any())

    def test_drop_missing_values(self):
        df = create_dataframe_with_missing_values()
        dropped_df = drop_missing_values(df)
        self.assertFalse(dropped_df.isnull().values.any())


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
