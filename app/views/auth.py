import re
from collections import namedtuple
from datetime import datetime

from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from db.connection import Connection
from modals.model import Model

bp = Blueprint('auth', __name__, url_prefix='/auth')
db = Connection.instance()


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
    user_table = Model(db, 'user_table')
    user_table.create(new_user)
    return jsonify(
        message="Registration Successful"
        ), 201
