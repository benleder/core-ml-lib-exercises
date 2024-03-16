import pandas as pd
import os
import unittest


# Method to read a CSV file
def read_csv_file(file_path):
    return pd.read_csv(file_path)


# Method to write a DataFrame to a CSV file
def write_csv_file(df, file_path):
    df.to_csv(file_path, index=False)


# Method to read an Excel file
def read_excel_file(file_path):
    return pd.read_excel(file_path)


# Method to write a DataFrame to an Excel file
def write_excel_file(df, file_path):
    df.to_excel(file_path, index=False)


# Method to read a JSON file
def read_json_file(file_path):
    return pd.read_json(file_path)


# Method to write a DataFrame to a JSON file
def write_json_file(df, file_path):
    df.to_json(file_path)


# Unit Tests
class TestReadWriteDataMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_data = {
            'Column1': [1, 2, 3],
            'Column2': ['A', 'B', 'C']
        }
        cls.test_df = pd.DataFrame(cls.test_data)

        cls.test_csv_file = 'test.csv'
        cls.test_excel_file = 'test.xlsx'
        cls.test_json_file = 'test.json'

    def test_read_write_csv_file(self):
        write_csv_file(self.test_df, self.test_csv_file)
        df_read = read_csv_file(self.test_csv_file)
        pd.testing.assert_frame_equal(df_read, self.test_df)

    def test_read_write_excel_file(self):
        write_excel_file(self.test_df, self.test_excel_file)
        df_read = read_excel_file(self.test_excel_file)
        pd.testing.assert_frame_equal(df_read, self.test_df)

    def test_read_write_json_file(self):
        write_json_file(self.test_df, self.test_json_file)
        df_read = read_json_file(self.test_json_file)
        pd.testing.assert_frame_equal(df_read, self.test_df)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_csv_file)
        os.remove(cls.test_excel_file)
        os.remove(cls.test_json_file)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
