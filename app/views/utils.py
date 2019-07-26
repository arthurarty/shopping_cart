def create_user_dict(user_tuple):
    """return a user dictionary provided a tuple"""
    if user_tuple is not None:
        return {
            'id': user_tuple[0],
            'email': user_tuple[1],
            'password': user_tuple[2],
            'date_created': user_tuple[3]
        }
    else:
        return None


def create_product_dict(product_tuple):
    if product_tuple is not None:
        return {
            'id': product_tuple[0],
            'name': product_tuple[1],
            'price': product_tuple[2],
            'date_created': product_tuple[3]
        }
    else:
        return None
