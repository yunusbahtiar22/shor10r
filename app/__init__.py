import os
from flask import Flask
from app.extension import db
from app.routes import short


# db = SQLAlchemy()


def create_app():
    # instanciate the app
    app = Flask(__name__)

    # app configurations
    app.config.from_object('app.config.Config')

    # setup extensions
    db.init_app(app)

    # register blueprint
    app.register_blueprint(short)

    return app
