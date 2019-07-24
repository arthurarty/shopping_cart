from db.driver import handle_operation


class Model():

    def __init__(self, db_conn, table_name):
        self.db_conn = db_conn
        self.table_name = table_name

    def create(self, col_values):
        """create a new record"""
        return handle_operation(
            'Insert', self.db_conn, self.table_name, col_values
            )

    def update(self, col_values):
        """update an existing record"""
        return handle_operation(
            'Update', self.db_conn, self.table_name, col_values
            )

    def delete(self, col_values):
        """hard delete record from the database"""
        return handle_operation(
            'Delete', self.db_conn, self.table_name, col_values
            )

    def find_all(self, col_values):
        """return all records in the database"""
        return handle_operation(
            'Select', self.db_conn, self.table_name, col_values
            )
