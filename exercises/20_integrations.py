from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import sqlalchemy


# Example function for data preprocessing
def preprocess_data_for_ml(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test


# Example usage
# Assuming df is your DataFrame and 'target' is your target column
# X_train, X_test, y_train, y_test = preprocess_data_for_ml(df, 'target')




# Example function to read data from SQL database
def read_data_from_sql(db_connection_string, query):
    engine = sqlalchemy.create_engine(db_connection_string)
    return pd.read_sql_query(query, engine)


# Example function to write data to SQL database
def write_data_to_sql(df, db_connection_string, table_name, if_exists='replace'):
    engine = sqlalchemy.create_engine(db_connection_string)
    df.to_sql(table_name, engine, if_exists=if_exists, index=False)


# Example usage
# db_connection_string = 'sqlite:///your_database.db'
# query = 'SELECT * FROM your_table'
# df = read_data_from_sql(db_connection_string, query)
# write_data_to_sql(df, db_connection_string, 'new_table')

class TestSklearnIntegration(unittest.TestCase):

    def test_preprocess_data_for_ml(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [4, 3, 2, 1],
            'target': [0, 1, 0, 1]
        })

        X_train, X_test, y_train, y_test = preprocess_data_for_ml(df, 'target')
        self.assertEqual(X_train.shape[1], df.shape[1] - 1)  # Check if target column is dropped
        self.assertEqual(len(X_train), len(y_train))  # Check if train data points and labels match

    def test_read_write_sql(self):
        # This is a simplistic test and requires a proper database setup to work
        db_connection_string = 'sqlite:///:memory:'
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        table_name = 'test_table'

        try:
            write_data_to_sql(df, db_connection_string, table_name)
            df_read = read_data_from_sql(db_connection_string, f'SELECT * FROM {table_name}')
            operation_successful = True
        except Exception:
            operation_successful = False

        self.assertTrue(operation_successful)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
