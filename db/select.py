from db.operation import Operation


class Select(Operation):
    """Handles selecting item from a table"""

    def __init__(self, db_conn, table_name):
        super().__init__(db_conn, table_name)

    def execute(self):
        """return all records in a given table"""
        self.db_conn.cur.execute(f"SELECT * FROM {self.table_name}")
        return self.db_conn.cur.fetchall()
