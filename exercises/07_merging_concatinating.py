import pandas as pd
import unittest


# Method to create two DataFrames with a common column
def create_dataframes_with_common_column():
    df1 = pd.DataFrame({
        'CommonColumn': [1, 2, 3],
        'ColumnA': ['A1', 'A2', 'A3']
    })
    df2 = pd.DataFrame({
        'CommonColumn': [2, 3, 4],
        'ColumnB': ['B2', 'B3', 'B4']
    })
    return df1, df2


# Method to perform inner merge
def perform_inner_merge(df1, df2, on_column):
    return pd.merge(df1, df2, on=on_column, how='inner')


# Method to perform outer merge
def perform_outer_merge(df1, df2, on_column):
    return pd.merge(df1, df2, on=on_column, how='outer')


# Method to concatenate DataFrames vertically
def concatenate_dataframes_vertically(df1, df2):
    return pd.concat([df1, df2], axis=0)


# Method to concatenate DataFrames horizontally
def concatenate_dataframes_horizontally(df1, df2):
    return pd.concat([df1, df2], axis=1)


# Unit Tests
class TestMergeConcatenateDataFrames(unittest.TestCase):

    def test_inner_outer_merge(self):
        df1, df2 = create_dataframes_with_common_column()

        # Inner Merge
        inner_merged_df = perform_inner_merge(df1, df2, 'CommonColumn')
        self.assertEqual(inner_merged_df.shape, (2, 3))

        # Outer Merge
        outer_merged_df = perform_outer_merge(df1, df2, 'CommonColumn')
        self.assertEqual(outer_merged_df.shape, (4, 3))

    def test_concatenate_dataframes(self):
        df1, df2 = create_dataframes_with_common_column()

        # Vertical Concatenation
        vertically_concatenated_df = concatenate_dataframes_vertically(df1, df2)
        self.assertEqual(vertically_concatenated_df.shape, (6, 3))

        # Horizontal Concatenation
        horizontally_concatenated_df = concatenate_dataframes_horizontally(df1, df2)
        self.assertEqual(horizontally_concatenated_df.shape, (3, 4))


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
