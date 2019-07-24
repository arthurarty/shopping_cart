from db.insert import Insert
from db.select import Select
from db.update import Update
from db.delete import Delete
from db.connection import Connection
from collections import namedtuple


def get_db_operations():
    operations = (Insert, Select, Update, Delete)
    return dict([cls.name, cls] for cls in operations)


def parse_operations(operations, op_name, db_conn, table_name, col_values):
    operation = operations.get(op_name)
    return operation(db_conn, table_name, col_values)

db_conn = Connection.instance()
Table = namedtuple('Table', 'id name age')
operations = get_db_operations()
operation = parse_operations(operations, 'Select', db_conn, 'company', Table)
print(operation.execute())
