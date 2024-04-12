import pandas as pd
import numpy as np
import unittest


# Method to create DataFrame with DateTime index
def create_dataframe_with_datetime_index(start, end, freq, data_column):
    date_range = pd.date_range(start=start, end=end, freq=freq)
    data = np.random.randn(len(date_range))
    return pd.DataFrame(data, index=date_range, columns=[data_column])


# Method to resample data
def resample_data(df, new_freq, resample_method='mean'):
    return df.resample(new_freq).apply(resample_method)


# Method to calculate rolling statistics
def calculate_rolling_statistics(df, column, window, statistics='mean'):
    if statistics == 'mean':
        return df[column].rolling(window=window).mean()
    elif statistics == 'std':
        return df[column].rolling(window=window).std()
    else:
        raise ValueError("Statistics argument must be 'mean' or 'std'")


# Method to filter data by date range
def filter_data_by_date_range(df, start_date, end_date):
    return df[start_date:end_date]


# Unit Tests
class TestTimeSeriesMethods(unittest.TestCase):

    def setUp(self):
        self.df = create_dataframe_with_datetime_index('2023-01-01', '2023-12-31', 'D', 'Data')

    def test_resample_data(self):
        resampled_df = resample_data(self.df, 'M')
        self.assertEqual(len(resampled_df), 12)  # 12 months in a year

    def test_calculate_rolling_statistics(self):
        rolling_mean = calculate_rolling_statistics(self.df, 'Data', 30, 'mean')
        self.assertEqual(len(rolling_mean.dropna()), len(self.df) - 29)

    def test_filter_data_by_date_range(self):
        filtered_df = filter_data_by_date_range(self.df, '2023-06-01', '2023-06-30')
        self.assertEqual(len(filtered_df), 30)  # 30 days in June


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
