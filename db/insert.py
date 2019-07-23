from db.operation import Operation
from db.utils import convertTuple, return_values


class Insert(Operation):
    """Handles creating a new record in the db"""

    def __init__(self, db_conn, table_name, cols_values):
        self.cols_values = cols_values
        super().__init__(db_conn, table_name)

    def execute(self):
        """Insert new record into database"""
        columns = convertTuple(self.cols_values._fields)
        values = [
            getattr(self.cols_values, x) for x in self.cols_values._fields
            ]
        str_values = return_values(values)
        self.db_conn.cur.execute(f"""
        INSERT INTO {self.table_name} ({columns})
        VALUES ({str_values})
        """)
        self.db_conn.commit_session()
