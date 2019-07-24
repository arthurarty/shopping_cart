from db.operation import Operation
from db.utils import convertTuple


class Select(Operation):
    """Handles selecting item from a table"""

    name = 'Select'

    def __init__(self, db_conn, table_name, cols_values):
        super().__init__(db_conn, table_name, cols_values)

    def execute(self):
        """return all records in a given table"""
        columns = convertTuple(self.cols_values._fields)
        self.db_conn.cur.execute(f"SELECT {columns} FROM {self.table_name}")
        return self.db_conn.cur.fetchall()
