from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    """Use app factory to create flask application"""
    app = Flask(__name__)

    from .views import auth
    app.register_blueprint(auth.bp)
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
    jwt = JWTManager(app)

    return app
