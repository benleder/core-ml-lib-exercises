import pandas as pd
import unittest

# Function to group data by multiple columns
def group_by_multiple_columns(df, group_columns):
    return df.groupby(group_columns)

# Function to apply custom aggregation
def apply_custom_aggregation(grouped_data, agg_func):
    return grouped_data.agg(agg_func)

# Function to filter groups
def filter_groups(df, group_columns, filter_func):
    return df.groupby(group_columns).filter(filter_func)

# Function to explore group operations (transform and apply)
def explore_group_operations(df, group_columns, operation, op_func):
    grouped = df.groupby(group_columns)
    if operation == 'transform':
        return grouped.transform(op_func)
    elif operation == 'apply':
        return grouped.apply(op_func)
    else:
        raise ValueError("Operation must be 'transform' or 'apply'")

# Unit Tests
class TestAdvancedGroupOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'Category': ['A', 'A', 'B', 'B', 'C'],
            'Subcategory': ['X', 'Y', 'X', 'Y', 'X'],
            'Values': [10, 20, 15, 25, 30]
        }
        cls.df = pd.DataFrame(cls.data)

    def test_group_by_multiple_columns(self):
        grouped = group_by_multiple_columns(self.df, ['Category', 'Subcategory'])
        self.assertTrue(isinstance(grouped, pd.core.groupby.DataFrameGroupBy))

    def test_apply_custom_aggregation(self):
        grouped = group_by_multiple_columns(self.df, ['Category'])
        agg_func = {'Values': ['sum', 'mean']}
        aggregated = apply_custom_aggregation(grouped, agg_func)
        self.assertEqual(aggregated.loc['A', ('Values', 'sum')], 30)

    def test_filter_groups(self):
        filter_func = lambda x: x['Values'].sum() > 40
        filtered = filter_groups(self.df, 'Category', filter_func)
        self.assertEqual(len(filtered['Category'].unique()), 2)

    def test_explore_group_operations(self):
        # Test transform
        op_func_transform = lambda x: x - x.mean()
        transformed = explore_group_operations(self.df, 'Category', 'transform', op_func_transform)
        self.assertEqual(len(transformed), len(self.df))

        # Test apply
        op_func_apply = lambda x: x.sort_values(by='Values', ascending=False)
        applied = explore_group_operations(self.df, 'Category', 'apply', op_func_apply)
        self.assertEqual(len(applied), len(self.df))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
