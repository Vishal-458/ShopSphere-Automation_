import sqlite3


class DBHelper:

    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(
            self.database_path
        )

    def execute_query(self, query: str, parameters=()):
        cursor = self.connection.cursor()

        cursor.execute(
            query,
            parameters
        )

        return cursor.fetchall()

    def execute_update(self, query: str, parameters=()):
        cursor = self.connection.cursor()

        cursor.execute(
            query,
            parameters
        )

        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()