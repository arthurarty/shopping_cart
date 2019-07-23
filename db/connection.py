import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


class Connection():
    """Class to create db connection"""

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT')
                )
            self.cur = self.conn.cursor()
        except:
            print("Database connection failed.")

    @staticmethod
    def instance():
        if '_instance' not in Connection.__dict__:
            Connection._instance = Connection()
        return Connection._instance

    def commit_session(self):
        """Commit session"""
        self.conn.commit()


class Table():
    """Class to handle creating tables"""

    def __init__(self, db, table_name, sql_query):
        self.table_name = table_name
        db.cur.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.table_name}
            ({sql_query});
            '''
        )
        db.commit_session()
