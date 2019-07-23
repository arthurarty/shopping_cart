from abc import ABC, abstractmethod


class Operation(ABC):
    """Abstract class for all db operations"""

    def __init__(self, db_conn, table_name):
        self.table_name = table_name
        self.db_conn = db_conn
        super().__init__()

    @abstractmethod
    def execute(self):
        pass
