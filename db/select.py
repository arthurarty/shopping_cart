from db.operation import Operation


class Select(Operation):
    """Handles selecting item from a table"""

    def __init__(self, table_name, db_conn):
        super().__init__(table_name, db_conn)

    def execute(self):
        self.db_conn.cur.execute(f"SELECT * FROM {self.table_name}")
        return self.db_conn.cur.fetchall()
