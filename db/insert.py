from db.operation import Operation


class Insert(Operation):
    """Handles creating a new record in the db"""

    def __init__(self, table_name, db_conn):
        super().__init__(table_name, db_conn)

    def execute(self):
        self.db_conn.cur.execute(f"SELECT * FROM {self.table_name}")
        return self.db_conn.cur.fetchall()
