from db.driver import handle_operation


class Model():

    def __init__(self, db_conn, table_name):
        self.db_conn = db_conn
        self.table_name = table_name

    def create(self, col_values):
        return handle_operation(
            'Insert', self.db_conn, self.table_name, col_values
            )

    def update(self, col_values):
        # update value in db
        pass

    def delete(self, col_values):
        # delete value from db
        pass

    def find_all(self, col_values):
        return handle_operation(
            'Select', self.db_conn, self.table_name, col_values
            )
