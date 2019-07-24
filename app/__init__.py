from flask import Flask


def create_app():
    """Use app factory to create flask application"""
    app = Flask(__name__)

    from .views import auth
    app.register_blueprint(auth.bp)

    return app
