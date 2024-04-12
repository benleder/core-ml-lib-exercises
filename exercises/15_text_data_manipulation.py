import pandas as pd
import unittest


# Function to create DataFrame with text data
def create_dataframe_with_text(data):
    return pd.DataFrame(data)


# Function to manipulate text data
def manipulate_text_data(df, column, operation, *args):
    if operation == 'split':
        return df[column].str.split(*args)
    elif operation == 'replace':
        return df[column].str.replace(*args)
    elif operation == 'contains':
        return df[column].str.contains(*args)
    else:
        raise ValueError("Operation not supported")


# Function to transform text to numerical data
def transform_text_to_numerical(df, column, word):
    return df[column].apply(lambda x: x.split().count(word))


# Unit Tests
class TestTextDataManipulationMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {'Text': ['hello world', 'hello pandas', 'hello numpy']}
        cls.df = create_dataframe_with_text(cls.data)

    def test_manipulate_text_data(self):
        # Test split
        split_data = manipulate_text_data(self.df, 'Text', 'split', ' ')
        self.assertEqual(len(split_data[0]), 2)

        # Test replace
        replaced_data = manipulate_text_data(self.df, 'Text', 'replace', 'hello', 'hi')
        self.assertTrue('hi' in replaced_data[0])

        # Test contains
        contains_data = manipulate_text_data(self.df, 'Text', 'contains', 'pandas')
        self.assertTrue(contains_data[1])

    def test_transform_text_to_numerical(self):
        count_word = transform_text_to_numerical(self.df, 'Text', 'hello')
        self.assertEqual(count_word[0], 1)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
