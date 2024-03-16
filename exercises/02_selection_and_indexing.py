import pandas as pd
import unittest
from typing import List


# Select a single column from a dataframe using that column's name
def select_single_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    return df[column_name]


# Select multiple columns from a dataframe using a list of colum names
def select_multiple_columns(df: pd.DataFrame, column_list: List) -> pd.DataFrame:
    return df[column_list]


# Select and individual row by using its index
def select_row_by_index(df: pd.DataFrame, index: int) -> pd.DataFrame:
    return df.iloc[index]


# Select all rows where a given colum is greater than the condition
def filter_dataframe(df: pd.DataFrame, column_name: str, condition: int) -> pd.DataFrame:
    return df[df[column_name] > condition]


# Given a dataframe of products, filter for only products that are low fat and recyclable
# Products Table:
# +-------------+----------+------------+
# | product_id  | low_fats | recyclable |
# +-------------+----------+------------+
# | 0           | Y        | N          |
# | 1           | Y        | Y          |
# | 2           | N        | Y          |
# | 3           | Y        | Y          |
# | 4           | N        | N          |
# +-------------+----------+------------+
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    r_and_l = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return r_and_l


class TestDataSelectionMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dict = {
            'Column1': [1, 2, 3, 4, 5],
            'Column2': ['A', 'B', 'C', 'D', 'E'],
            'Column3': [10, 20, 30, 40, 50]
        }
        cls.df = pd.DataFrame(cls.data_dict)

    def test_select_single_column(self):
        selected_column = select_single_column(self.df, 'Column2')
        self.assertTrue(all(selected_column == self.df['Column2']))

    def test_select_multiple_columns(self):
        selected_columns = select_multiple_columns(self.df, ['Column1', 'Column3'])
        self.assertListEqual(list(selected_columns.columns), ['Column1', 'Column3'])

    def test_select_row_by_index(self):
        selected_row = select_row_by_index(self.df, 2)
        expected_row = self.df.iloc[2]
        pd.testing.assert_series_equal(selected_row, expected_row)

    def test_filter_dataframe(self):
        filtered_df = filter_dataframe(self.df, 'Column3', 25)
        self.assertTrue(all(filtered_df['Column3'] > 25))

    def test_find_products(self):
        data = {
            'product_id': [0, 1, 2, 3, 4],
            'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
            'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
        }
        df = pd.DataFrame(data)
        result = find_products(df)
        expected_output = df[(df['low_fats'] == 'Y') & (df['recyclable'] == 'Y')]
        pd.testing.assert_frame_equal(result, expected_output)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
