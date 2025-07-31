import sqlite3
import pandas as pd
from datawrangler import DataWrangler


class Database:
    def __init__(self, db_name):
        """Initialize the database connection"""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
    
    def create_table(self, table_name, columns):
        """
        Create a table with the specified columns.
        Args:
        - table_name (str): The name of the table.
        - columns (dict): A dictionary where the key is the column name and the value is the data type.
        """
        columns_str = ', '.join([f'"{col}" {dtype}' for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});"
        self.cursor.execute(query)
        # self.connection.commit()
    
    def insert_data(self, table_name, csv_file_path):
        """
        Insert CSV data into a table.
        """
        data = pd.read_csv(csv_file_path)
        data.to_sql(table_name, self.connection, if_exists='append', index = False)

    
    def fetch_data(self, table_name, columns="*", condition=None):
        """
        Fetch data from a table.
        Args:
        - table_name (str): The name of the table.
        - columns (str or list): The columns to fetch, default is '*'.
        - condition (str): Optional SQL condition (e.g., "WHERE id=1").
        """
        if isinstance(columns, list):
            columns = ', '.join(columns)
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close(self):
        """Close the database connection"""
        self.connection.close()


db = Database("/Users/anshagarwal/GitHub /Virtual Library/Book-Rec-AI/data/BooksInventory.db")
dw = DataWrangler("/Users/anshagarwal/GitHub /Virtual Library/Book-Rec-AI/data/Books.csv")
schema = dw.get_col_dtypes()
db.create_table("BookInventory", schema)
db.insert_data("BookInventory", "/Users/anshagarwal/GitHub /Virtual Library/Book-Rec-AI/data/Books.csv")
print(db.fetch_data("BookInventory"))
