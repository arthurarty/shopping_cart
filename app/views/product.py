import re
from collections import namedtuple
from datetime import datetime

from flask import Blueprint, jsonify, request

from db.connection import Connection
from models.product_model import ProductModel

bp = Blueprint('product', __name__, url_prefix='/product')
db_conn = Connection.instance()


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
    product_table = ProductModel(db_conn)
    product_table.create(new_product)
    return jsonify(
        message="Product Successful"
    ), 201


@bp.route('/', methods=['GET'])
def all_products():
    """Get all products"""
    product_table = ProductModel(db_conn)
    all_products = product_table.find_all()
    return jsonify(
        products=all_products
    ), 200


@bp.route('/<int:product_id>', methods=['GET'])
def single_product(product_id):
    """return a single product given its id"""
    product = ProductModel(db_conn)
    selected_product = product.find(product_id)
    if selected_product is None:
        return jsonify(message="Product not found"), 404
    return jsonify(
        product=selected_product
    ), 200


@bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """delete product from system"""
    product = ProductModel(db_conn)
    Columns = namedtuple('Columns', 'id')
    del_product = Columns(id=product_id)
    product.delete(del_product)
    return jsonify(
        message=f"Product {product_id} has been deleted"
    ), 200


@bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """update a product given its id"""
    request_data = request.get_json()
    name = request_data['name']
    price = request_data['price']
    product = ProductModel(db_conn)
    Row_update = namedtuple('Row_Update', 'id name price')
    product_update = Row_update(id=product_id, name=name, price=price)
    product.update(product_update)
    return jsonify(
        message=f"Product {product_id} has been updated"
    ), 200
