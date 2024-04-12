import unittest
import pandas as pd


# Function to calculate correlation between two columns
def calculate_correlation(df, column1, column2):
    return df[column1].corr(df[column2])


# Function to explore data with describe
def explore_data_with_describe(df):
    return df.describe()


# Function to identify and handle outliers
def identify_and_handle_outliers(df, column, method='mean', threshold=1.5):
    if method == 'mean':
        mean = df[column].mean()
        std = df[column].std()
        upper_bound = mean + threshold * std
        lower_bound = mean - threshold * std
    elif method == 'quantile':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        upper_bound = Q3 + threshold * IQR
        lower_bound = Q1 - threshold * IQR
    else:
        raise ValueError("Method must be 'mean' or 'quantile'")

    outliers = df[(df[column] > upper_bound) | (df[column] < lower_bound)]
    df_without_outliers = df.drop(outliers.index)
    return df_without_outliers


# Unit Tests
class TestAdvancedDataAnalysisMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'Column1': [1, 2, 3, 4, 5, 100],
            'Column2': [10, 20, 30, 40, 50, 60]
        }
        cls.df = pd.DataFrame(cls.data)

    def test_calculate_correlation(self):
        correlation = calculate_correlation(self.df, 'Column1', 'Column2')
        self.assertTrue(isinstance(correlation, float))

    def test_explore_data_with_describe(self):
        description = explore_data_with_describe(self.df)
        self.assertTrue(isinstance(description, pd.DataFrame))

    def test_identify_and_handle_outliers(self):
        handled_df = identify_and_handle_outliers(self.df, 'Column1', method='mean')
        self.assertFalse(handled_df['Column1'].max() > 100)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
