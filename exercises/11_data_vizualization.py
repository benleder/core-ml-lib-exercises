import unittest
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import seaborn as sns


# Function to generate a line plot for time series data
def generate_line_plot(df, x_column, y_column, title):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_column], df[y_column])
    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()


# Function to create a bar chart for group-wise aggregated data
def create_bar_chart(df, group_by_column, target_column, agg_func, title):
    aggregated_data = df.groupby(group_by_column)[target_column].agg(agg_func)
    aggregated_data.plot(kind='bar')
    plt.title(title)
    plt.ylabel(target_column)
    plt.show()


# Function to visualize a histogram
def visualize_histogram(df, column, bins, title):
    df[column].plot(kind='hist', bins=bins)
    plt.title(title)
    plt.xlabel(column)
    plt.show()


# Function to create an advanced visualization (using Seaborn)
def create_advanced_visualization(df, plot_type, title, **kwargs):
    plt.figure(figsize=(10, 6))
    if plot_type == 'heatmap':
        sns.heatmap(df, **kwargs)
    elif plot_type == 'pairplot':
        sns.pairplot(df, **kwargs)
    plt.title(title)
    plt.show()


class TestVisualizationFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a sample DataFrame for testing
        data = {'Date': pd.date_range(start='1/1/2021', periods=5, freq='D'),
                'Value': [1, 3, 2, 5, 4],
                'Category': ['A', 'B', 'A', 'B', 'C']}
        cls.df = pd.DataFrame(data)

    def test_generate_line_plot(self):
        plt.figure()
        generate_line_plot(self.df, 'Date', 'Value', 'Test Line Plot')
        self.assertIsInstance(plt.gca(), Axes)

    def test_create_bar_chart(self):
        plt.figure()
        create_bar_chart(self.df, 'Category', 'Value', 'sum', 'Test Bar Chart')
        self.assertIsInstance(plt.gca(), Axes)

    def test_visualize_histogram(self):
        plt.figure()
        visualize_histogram(self.df, 'Value', 5, 'Test Histogram')
        self.assertIsInstance(plt.gca(), Axes)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
