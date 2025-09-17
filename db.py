import os
import pandas as pd
import psycopg2

class DB:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conm = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)

    def create_table(self, table_name, columns):
        cursor = self.conm.cursor()
        # Define columns as 'name TYPE' (default to TEXT for demo)
        columns_def = ', '.join([f'"{col}" TEXT' for col in columns])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})")
        self.conm.commit()
        cursor.close()

    def insert_data(self, table_name, df):
        cursor = self.conm.cursor()
        for i, row in df.iterrows():
            cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})", tuple(row))
        self.conm.commit()
        cursor.close()

    def execute_query(self, query):
        cursor = self.conm.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def select_all_data_from_table(self, table_name):
        cursor = self.conm.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        self.conm.close()
