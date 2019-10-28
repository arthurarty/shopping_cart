import os

from dotenv import load_dotenv
from flask import Flask, g
from flask_jwt_extended import JWTManager

from connection import Connection

load_dotenv()


def create_app():
    """Use app factory to create flask application"""
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    jwt = JWTManager(app)

    from .views import auth, product
    app.register_blueprint(auth.bp)
    app.register_blueprint(product.bp)

    return app
