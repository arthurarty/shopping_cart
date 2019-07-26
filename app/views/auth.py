import re
from collections import namedtuple
from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

from connection import Connection
from db.db_wrapper import DBWrapper
from app.views.utils import create_user_dict

bp = Blueprint('auth', __name__, url_prefix='/auth')
db_conn = Connection.instance()
user_table = DBWrapper(db_conn, 'user_table')


@bp.route('/signup', methods=['POST'])
def signup():
    """Registering a new user"""
    request_data = request.get_json()
    email = request_data['email']
    reg = re.match(
        '([a-zA-Z0-9]+)([.]*)([-]*)([a-zA-Z0-9]+)@{1}([a-z]+)\.([a-z]+)',
        email)
    if reg is None:
        return jsonify(message="Invalid email address"), 401
    password = request_data['password']
    # specify columns to insert data into
    Columns = namedtuple('Columns', 'email password date_created')
    new_user = Columns(
        email=email,
        password=generate_password_hash(password),
        date_created=str(datetime.now())
    )
    user_table.create(new_user)
    return jsonify(
        message="Registration Successful"
    ), 201


@bp.route('/login', methods=['POST'])
def login():
    """logging in an existing user"""
    request_data = request.get_json()
    email_address = request_data['email']
    password = request_data['password']
    Columns = namedtuple('Columns', 'email')
    user_details = Columns(email=email_address)
    user_tuple = user_table.select(user_details)
    user_dict = create_user_dict(user_tuple)
    if (user_dict is not None) and check_password_hash(user_dict['password'], password):
        access_token = create_access_token(identity=user_dict['email'])
        return jsonify(
            message="Login Successful", token=access_token
        ), 200
    else:
        return jsonify(message="Wrong username or password"), 401
