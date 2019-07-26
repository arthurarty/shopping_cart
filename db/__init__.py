from abc import ABC, abstractmethod
from db.utils import convertTuple, return_values


class DB(ABC):
    """Abstract DB class to handle db operations"""

    def __init__(self, db_conn, table_name):
        self.db_conn = db_conn
        self.table_name = table_name
        super().__init__()

    @abstractmethod
    def create(self, cols_values):
        """inserts data into the database"""
        pass

    @abstractmethod
    def update(self, cols_values):
        """updates an existing row"""
        pass

    @abstractmethod
    def select(self, cols_values):
        """return a single record from the table"""
        pass

    @abstractmethod
    def select_all(self, cols_values):
        """Select all records in a table"""
        pass

    @abstractmethod
    def delete(self, cols_values):
        """deletes a record from the database"""
        pass
