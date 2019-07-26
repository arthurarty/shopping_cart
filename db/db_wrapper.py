from db import DB
from db.utils import convertTuple, return_values, sql_from_dict


class DBWrapper(DB):
    """Class that implements the Db interface"""

    def __init__(self, db_conn, table_name):
        super().__init__(db_conn, table_name)

    def create(self, cols_values):
        """insert record into a given table"""
        columns = convertTuple(cols_values._fields)
        values = [
            getattr(cols_values, x) for x in cols_values._fields
            ]
        str_values = return_values(values)
        self.db_conn.cur.execute(f"""
        INSERT INTO {self.table_name} ({columns})
        VALUES ({str_values})
        """)
        self.db_conn.commit_session()

    def select(self, cols_values):
        """return a single records in a given table"""
        dict_values = dict(cols_values._asdict())
        identifier = sql_from_dict(dict_values)
        self.db_conn.cur.execute(f"""
            SELECT * FROM {self.table_name}
            WHERE {identifier}
            """)
        return self.db_conn.cur.fetchone()

    def select_all(self, cols_values):
        """return all records in a table"""
        columns = convertTuple(cols_values._fields)
        self.db_conn.cur.execute(f"SELECT {columns} FROM {self.table_name}")
        return self.db_conn.cur.fetchall()

    def update(self, cols_values):
        dict_values = dict(cols_values._asdict())
        table_id = dict_values.pop('id')
        values_to_set = sql_from_dict(dict_values)
        self.db_conn.cur.execute(f"""
        UPDATE {self.table_name} SET {values_to_set}
        WHERE id = {table_id}
        """)
        self.db_conn.commit_session()

    def delete(self, cols_values):
        """Delete a record by its id"""
        record_id = cols_values.id
        self.db_conn.cur.execute(f"""
        DELETE FROM {self.table_name}
        WHERE id = {record_id}
        """)
        self.db_conn.commit_session()
