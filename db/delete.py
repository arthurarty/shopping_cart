from db.operation import Operation


class Delete(Operation):
    """Handles deleting a record from the database"""

    name = 'Delete'

    def __init__(self, db_conn, table_name, cols_values):
        super().__init__(db_conn, table_name, cols_values)

    def execute(self):
        """Delete a record by its id"""
        table_id = self.cols_values.id
        self.db_conn.cur.execute(f"""
        DELETE FROM {self.table_name}
        WHERE id = {table_id}
        """)
        self.db_conn.commit_session()
