from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    """Use app factory to create flask application"""
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
    jwt = JWTManager(app)

    from .views import auth, product
    app.register_blueprint(auth.bp)
    app.register_blueprint(product.bp)

    return app
