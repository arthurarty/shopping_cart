from db.insert import Insert
from db.select import Select
from db.update import Update
from db.delete import Delete
from db.connection import Connection
from collections import namedtuple


def get_db_operations():
    """create a dict containing the operations and their classess"""
    operations = (Insert, Select, Update, Delete)
    return dict([cls.name, cls] for cls in operations)


def parse_operations(operations, op_name, db_conn, table_name, col_values):
    """select an operation and return it with the arguments"""
    operation = operations.get(op_name)
    return operation(db_conn, table_name, col_values)


def handle_operation(op_name, db_conn, table_name, col_values):
    """handles execution of operation"""
    operations = get_db_operations()
    operation = parse_operations(
        operations, op_name, db_conn, table_name, col_values
        )
    return operation.execute()
