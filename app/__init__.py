from flask import Flask
from .extensions import db
from .routes import main


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bennys_pizza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
<<<<<<< HEAD
    # # Making sure we are within the application context when creating tables
    # with app.app_context():
    #     db.create_all() # Creating tables for our data models
=======
    # Making sure we are within the application context when creating tables
    with app.app_context():
        db.create_all() # Creating tables for our data models
>>>>>>> f6e033f9f666e7ea67e374324f7c50bfb4b8aa25

    app.register_blueprint(main)

    return app

