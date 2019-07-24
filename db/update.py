from db.operation import Operation
from db.utils import sql_from_dict


class Update(Operation):
    """Handles updating a record with its id specified"""

    name = 'Update'

    def __init__(self, db_conn, table_name, cols_values):
        super().__init__(db_conn, table_name, cols_values)

    def execute(self):
        """Update existing record by its id"""
        dict_values = dict(self.cols_values._asdict())
        table_id = dict_values.pop('id')
        values_to_set = sql_from_dict(dict_values)
        self.db_conn.cur.execute(f"""
        UPDATE {self.table_name} SET {values_to_set}
        WHERE id = {table_id}
        """)
        self.db_conn.commit_session()
