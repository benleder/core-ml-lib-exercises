import pandas as pd
import unittest
from typing import List
from typing import Callable


# Append a new colum to a dataframe
def add_new_column(df: pd.DataFrame, column_name: str, data: List) -> pd.DataFrame:
    df[column_name] = data
    return df


# Apply a lambda function to a column in the data frame
def modify_column(df: pd.DataFrame, column_name: str, operation: Callable[[int], int]) -> pd.DataFrame:
    df[column_name] = df[column_name].apply(operation)
    return df


# Given a column name, drop that column from the dataframe
def drop_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    return df.drop(columns=[column_name])


# Given a column name, sort the dataframe by that particular column
def sort_dataframe(df: pd.DataFrame, sort_by_column, ascending=True) -> pd.DataFrame:
    return df.sort_values(by=sort_by_column, ascending=ascending)


class TestDataManipulationMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dict = {
            'Column1': [1, 2, 3, 4, 5],
            'Column2': [10, 20, 30, 40, 50]
        }
        cls.df = pd.DataFrame(cls.data_dict)

    def test_add_new_column(self):
        new_column_data = [5, 4, 3, 2, 1]
        modified_df = add_new_column(self.df.copy(), 'Column3', new_column_data)
        self.assertTrue('Column3' in modified_df)

    def test_modify_column(self):
        operation = lambda x: x * 2
        modified_df = modify_column(self.df.copy(), 'Column1', operation)
        self.assertTrue(all(modified_df['Column1'] == self.df['Column1'] * 2))

    def test_drop_column(self):
        modified_df = drop_column(self.df.copy(), 'Column1')
        self.assertFalse('Column1' in modified_df)

    def test_sort_dataframe(self):
        sorted_df = sort_dataframe(self.df.copy(), 'Column2', False)
        self.assertTrue(all(sorted_df['Column2'] == self.df['Column2'][::-1]))


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
