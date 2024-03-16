import pandas as pd
import matplotlib.pyplot as plt
import unittest


# Method to calculate basic statistics
def calculate_basic_statistics(df, column_name):
    mean = df[column_name].mean()
    median = df[column_name].median()
    std_dev = df[column_name].std()
    return mean, median, std_dev


# Method to group data and calculate statistics
def group_data_and_calculate_statistics(df, group_column, target_column, statistic):
    grouped_data = df.groupby(group_column)[target_column].agg(statistic)
    return grouped_data


# Method to create a simple plot
def create_simple_plot(df, column_name, plot_type='line'):
    if plot_type == 'bar':
        df[column_name].plot(kind='bar')
    else:  # default to line plot
        df[column_name].plot(kind='line')
    plt.show()


# Unit Tests
class TestBasicDataAnalysisMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dict = {
            'Category': ['A', 'A', 'B', 'B', 'C'],
            'Values': [1, 3, 5, 7, 9]
        }
        cls.df = pd.DataFrame(cls.data_dict)

    def test_calculate_basic_statistics(self):
        mean, median, std_dev = calculate_basic_statistics(self.df, 'Values')
        self.assertEqual(mean, self.df['Values'].mean())
        self.assertEqual(median, self.df['Values'].median())
        self.assertEqual(std_dev, self.df['Values'].std())

    def test_group_data_and_calculate_statistics(self):
        grouped_mean = group_data_and_calculate_statistics(self.df, 'Category', 'Values', 'mean')
        expected_result = self.df.groupby('Category')['Values'].mean()
        pd.testing.assert_series_equal(grouped_mean, expected_result)


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
