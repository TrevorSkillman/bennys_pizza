""" This file initializes the Flask App for Benny's Pizza.
    It sets up the database configuration and registers blueprints.
"""

from flask import Flask
from .extensions import db
from .routes import main


def create_app():
    """
    Create and configures the Flask app.

    Retruns:
        app: configured Flask app instance.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bennys_pizza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'supersecretkey'

    db.init_app(app)

    app.register_blueprint(main)

    return app

