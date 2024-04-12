import pandas as pd
import numpy as np
import unittest


# Function to apply a rolling window function
def apply_rolling_window_function(df, column, window_size, function='mean'):
    if function == 'mean':
        return df[column].rolling(window=window_size).mean()
    # Add more functions as needed
    else:
        raise ValueError("Function not supported")


# Function to use an expanding window
def use_expanding_window(df, column, function='sum'):
    if function == 'sum':
        return df[column].expanding().sum()
    # Add more functions as needed
    else:
        raise ValueError("Function not supported")


# Function to calculate exponential moving average
def calculate_exponential_moving_average(df, column, span):
    return df[column].ewm(span=span).mean()


# Unit Tests
class TestWindowFunctionsExpandingOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {'Value': np.random.rand(100)}  # Random data for testing
        cls.df = pd.DataFrame(data)

    def test_apply_rolling_window_function(self):
        rolling_mean = apply_rolling_window_function(self.df, 'Value', 5)
        self.assertEqual(len(rolling_mean.dropna()), len(self.df) - 4)

    def test_use_expanding_window(self):
        expanding_sum = use_expanding_window(self.df, 'Value')
        self.assertEqual(expanding_sum.iloc[-1], sum(self.df['Value']))

    def test_calculate_exponential_moving_average(self):
        ema = calculate_exponential_moving_average(self.df, 'Value', 10)
        self.assertEqual(len(ema), len(self.df))


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
