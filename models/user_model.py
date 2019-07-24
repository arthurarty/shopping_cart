from collections import namedtuple

from models.model import Model


class UserModel(Model):
    """A model for the user table"""

    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.table_name = 'user_table'
        super().__init__(self.db_conn, self.table_name)

    def user_dict(self, email_address):
        Columns = namedtuple('Columns', 'email')
        user_details = Columns(email=email_address)
        user_tuple = self.find(user_details)
        if user_tuple is not None:
            return {
                'id': user_tuple[0],
                'email': user_tuple[1],
                'password': user_tuple[2],
                'date_created': user_tuple[3]
            }
        else:
            return None
