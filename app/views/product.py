import re
from collections import namedtuple
from datetime import datetime

from flask import Blueprint, jsonify, request

from connection import Connection
from db.db_wrapper import DBWrapper
from app.views.utils import create_product_dict

bp = Blueprint('product', __name__, url_prefix='/product')
db_conn = Connection.instance()
product_table = DBWrapper(db_conn, 'product')


@bp.route('/', methods=['POST'])
def create():
    """Add new product"""
    request_data = request.get_json()
    name = request_data['name']
    price = request_data['price']
    # specify columns to insert data into
    Columns = namedtuple('Columns', 'name price date_created')
    new_product = Columns(
        name=name,
        price=price,
        date_created=str(datetime.now())
    )
    product_table.create(new_product)
    return jsonify(
        message="Product Successful"
    ), 201


@bp.route('/', methods=['GET'])
def all_products():
    """Get all products"""
    Columns = namedtuple('Columns', 'id name price date_created')
    product_list = []
    for product in product_table.select_all(Columns):
        product_list.append({
            'id': product[0],
            'name': product[1],
            'price': product[2],
            'date_created': product[3]
        })
    return jsonify(
        products=product_list
    ), 200


@bp.route('/<int:product_id>', methods=['GET'])
def single_product(product_id):
    """return a single product given its id"""
    Columns = namedtuple('Columns', 'id')
    single_product = Columns(id=product_id)
    selected_product = product_table.select(single_product)
    product_dict = create_product_dict(selected_product)
    if product_dict is None:
        return jsonify(message="Product not found"), 404
    return jsonify(
        product=product_dict
    ), 200


@bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """delete product from system"""
    Columns = namedtuple('Columns', 'id')
    del_product = Columns(id=product_id)
    product_table.delete(del_product)
    return jsonify(
        message=f"Product {product_id} has been deleted"
    ), 200


@bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """update a product given its id"""
    request_data = request.get_json()
    name = request_data['name']
    price = request_data['price']
    Row_update = namedtuple('Row_Update', 'id name price')
    product_update = Row_update(id=product_id, name=name, price=price)
    product_table.update(product_update)
    return jsonify(
        message=f"Product {product_id} has been updated"
    ), 200
