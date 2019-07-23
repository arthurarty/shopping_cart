from db.select import Select
from db.insert import Insert


class Model():

    def __init__(self, db_conn, table_name):
        self.db_conn = db_conn
        self.table_name = table_name

    def create(self, col_values):
        record = Insert(self.db_conn, self.table_name, col_values)
        return record.execute()

    def update(self):
        # update value in db
        pass

    def delete(self):
        # delete value from db
        pass

    def find_all(self):
        records = Select(self.db_conn, self.table_name)
        return records.execute()