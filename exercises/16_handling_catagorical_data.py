import pandas as pd
import unittest


# Function to convert a column to categorical data
def convert_to_categorical(df, column):
    df[column] = df[column].astype('category')
    return df


# Function to explore properties of categorical data
def explore_categorical_properties(df, column):
    categories = df[column].cat.categories
    codes = df[column].cat.codes
    return categories, codes


# Function to create dummy variables
def create_dummy_variables(df, column):
    return pd.get_dummies(df, columns=[column])


# Unit Tests
class TestCategoricalDataMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {'Text': ['apple', 'banana', 'orange', 'apple', 'banana']}
        cls.df = pd.DataFrame(cls.data)

    def test_convert_to_categorical(self):
        categorical_df = convert_to_categorical(self.df, 'Text')
        self.assertTrue(pd.api.types.is_categorical_dtype(categorical_df['Text']))

    def test_explore_categorical_properties(self):
        categorical_df = convert_to_categorical(self.df, 'Text')
        categories, codes = explore_categorical_properties(categorical_df, 'Text')
        self.assertEqual(len(categories), 3)
        self.assertEqual(len(codes), len(self.df))

    def test_create_dummy_variables(self):
        categorical_df = convert_to_categorical(self.df, 'Text')
        dummy_df = create_dummy_variables(categorical_df, 'Text')
        self.assertEqual(len(dummy_df.columns), 3)  # 3 categories


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
