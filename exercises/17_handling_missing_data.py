# Redefining the test class and functions for missing and duplicate data, and then running the tests in the same cell
import pandas as pd
import unittest


# Function to count missing values
def count_missing_values(df):
    return df.isnull().sum()


# Function to impute missing data
def impute_missing_data(df, column, strategy='mean'):
    if strategy == 'mean':
        df[column].fillna(df[column].mean(), inplace=True)
    elif strategy == 'median':
        df[column].fillna(df[column].median(), inplace=True)
    elif strategy == 'mode':
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df


# Function to drop duplicates
def drop_duplicates(df):
    return df.drop_duplicates()


# Function to compare removal vs imputation
def compare_removal_vs_imputation(df, column, impute_strategy='mean'):
    # Removal
    removal_df = df.dropna(subset=[column])

    # Imputation
    impute_df = impute_missing_data(df.copy(), column, strategy=impute_strategy)

    return removal_df, impute_df


# Unit Tests
class TestMissingDuplicateDataMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'Column1': [1, 2, np.nan, 4, 5],
            'Column2': ['A', 'B', 'B', np.nan, 'E'],
            'Column3': [1, 1, 2, 2, np.nan]
        }
        cls.df = pd.DataFrame(cls.data)

    def test_count_missing_values(self):
        missing_counts = count_missing_values(self.df)
        self.assertEqual(missing_counts['Column1'], 1)
        self.assertEqual(missing_counts['Column2'], 1)

    def test_impute_missing_data(self):
        imputed_df = impute_missing_data(self.df.copy(), 'Column1', 'mean')
        self.assertFalse(imputed_df['Column1'].isnull().any())

    def test_drop_duplicates(self):
        df_with_duplicates = self.df.append(self.df)
        deduped_df = drop_duplicates(df_with_duplicates)
        self.assertEqual(len(deduped_df), len(self.df))

    def test_compare_removal_vs_imputation(self):
        removal_df, impute_df = compare_removal_vs_imputation(self.df.copy(), 'Column1', 'mean')
        self.assertNotEqual(len(removal_df), len(impute_df))


# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
