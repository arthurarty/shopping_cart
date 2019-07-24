from db.operation import Operation
from db.utils import sql_from_dict


class SelectOne(Operation):
    """Handles selecting a single item from a table"""

    name = 'SelectOne'

    def __init__(self, db_conn, table_name, cols_values):
        super().__init__(db_conn, table_name, cols_values)

    def execute(self):
        """return a single records in a given table"""
        dict_values = dict(self.cols_values._asdict())
        identifier = sql_from_dict(dict_values)
        self.db_conn.cur.execute(f"""
            SELECT * FROM {self.table_name}
            WHERE {identifier}
            """)
        return self.db_conn.cur.fetchone()
