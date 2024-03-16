import pandas as pd
import unittest


# Using the parameter of 'data',
# inject this dictionary into the constructor
# of the DataFrame object and return it
def create_dataframe(data: dict) -> pd.DataFrame:
    return pd.DataFrame(data)


class TestPandasDataFrameMethods(unittest.TestCase):

    def test_create_dataframe(self):
        data_dict = {
            'Column1': [1, 2, 3, 4, 5],
            'Column2': ['A', 'B', 'C', 'D', 'E'],
            'Column3': [True, False, True, False, True]
        }
        df = create_dataframe(data_dict)

        # assert that df has 5 rows across 3 columns
        self.assertEqual(df.shape, (5, 3))

        # assert df contains correct column names
        self.assertListEqual(list(df.columns), ['Column1', 'Column2', 'Column3'])


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
