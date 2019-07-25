from collections import namedtuple

from models.model import Model


class ProductModel(Model):
    """A model for the user table"""

    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.table_name = 'product'
        super().__init__(self.db_conn, self.table_name)

    def find(self, id):
        """creates a dictionary containing the product"""
        Columns = namedtuple('Columns', 'id')
        single_product = Columns(id=id)
        product_tuple = super().find(single_product)
        # todo: Consider a scenario where a new field is added
        if product_tuple is not None:
            return {
                'id': product_tuple[0],
                'name': product_tuple[1],
                'price': product_tuple[2],
                'date_created': product_tuple[3]
            }
        else:
            return None

    def find_all(self):
        """convert each item to a dictionary then make
        a list of the dictionaries
        """
        Columns = namedtuple('Columns', 'id name price date_created')
        all_products = []
        # todo: Consider a scenario where a new field is added
        for product in super().find_all(Columns):
            all_products.append({
                'id': product[0],
                'name': product[1],
                'price': product[2],
                'date_created': product[3]
            })
        return all_products
