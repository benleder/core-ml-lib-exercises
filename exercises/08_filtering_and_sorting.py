import pandas as pd
import unittest


# Method to filter DataFrame using multiple conditions
def filter_dataframe_multiple_conditions(df, condition1, condition2, logical_operator='and'):
    if logical_operator == 'and':
        return df[condition1 & condition2]
    elif logical_operator == 'or':
        return df[condition1 | condition2]
    else:
        raise ValueError("Logical operator must be 'and' or 'or'")


# Method to sort DataFrame using multiple columns
def sort_dataframe_multiple_columns(df, columns, ascending=True):
    return df.sort_values(by=columns, ascending=ascending)


# Method to filter based on criteria from another column
def filter_based_on_another_column(df, source_column, target_column, threshold):
    criterion = df[source_column] > threshold
    return df[df[target_column][criterion]]


# Unit Tests
class TestAdvancedFilteringSortingMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'Column1': [1, 2, 3, 4, 5],
            'Column2': [10, 9, 8, 7, 6],
            'Column3': [3, 4, 2, 5, 1]
        }
        cls.df = pd.DataFrame(cls.data)

    def test_filter_dataframe_multiple_conditions(self):
        condition1 = self.df['Column1'] > 2
        condition2 = self.df['Column2'] < 8
        filtered_df = filter_dataframe_multiple_conditions(self.df, condition1, condition2)
        self.assertEqual(len(filtered_df), 2)

    def test_sort_dataframe_multiple_columns(self):
        sorted_df = sort_dataframe_multiple_columns(self.df, ['Column3', 'Column1'])
        self.assertTrue(sorted_df.iloc[0]['Column1'], 5)
        self.assertTrue(sorted_df.iloc[1]['Column1'], 3)

    def test_filter_based_on_another_column(self):
        filtered_df = filter_based_on_another_column(self.df, 'Column1', 'Column2', 3)
        self.assertEqual(len(filtered_df), 2)


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
