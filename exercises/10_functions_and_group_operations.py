import pandas as pd
import unittest


# Method to apply a custom function to a column
def apply_custom_function(df, column, custom_function):
    return df[column].apply(custom_function)


# Method to group data and apply an aggregation function
def group_and_aggregate_data(df, group_by_column, target_column, agg_function):
    return df.groupby(group_by_column)[target_column].agg(agg_function)


# Method to create a pivot table
def create_pivot_table(df, index, columns, values, aggfunc='mean'):
    return pd.pivot_table(df, index=index, columns=columns, values=values, aggfunc=aggfunc)


# Unit Tests
class TestFunctionApplicationGroupOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'Category': ['A', 'A', 'B', 'B', 'C'],
            'Values': [10, 20, 15, 25, 30],
            'Subcategory': ['X', 'Y', 'X', 'Y', 'X']
        }
        cls.df = pd.DataFrame(cls.data)

    def test_apply_custom_function(self):
        custom_function = lambda x: x * 2
        modified_df = apply_custom_function(self.df, 'Values', custom_function)
        expected_result = self.df['Values'] * 2
        pd.testing.assert_series_equal(modified_df, expected_result)

    def test_group_and_aggregate_data(self):
        grouped_data = group_and_aggregate_data(self.df, 'Category', 'Values', 'sum')
        self.assertEqual(grouped_data['A'], 30)
        self.assertEqual(grouped_data['B'], 40)

    def test_create_pivot_table(self):
        pivot = create_pivot_table(self.df, index='Category', columns='Subcategory', values='Values')
        self.assertIn('X', pivot.columns)
        self.assertIn('Y', pivot.columns)


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
