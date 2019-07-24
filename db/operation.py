from abc import ABC, abstractmethod, abstractproperty


class Operation(ABC):
    """Abstract class for all db operations"""

    @abstractproperty
    def name(self):
        pass

    def __init__(self, db_conn, table_name, cols_values):
        self.db_conn = db_conn
        self.table_name = table_name
        self.cols_values = cols_values
        super().__init__()

    @abstractmethod
    def execute(self):
        pass
