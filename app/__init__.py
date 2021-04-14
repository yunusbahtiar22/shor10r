from flask import Flask
from app.ext import db
from app.routes import shortener


# db = SQLAlchemy()


def create_app():
    # instanciate the app
    app = Flask(__name__)

    # app configurations
    app.config.from_object('app.config.Config')

    # setup extensions
    db.init_app(app)

    # register blueprint
    app.register_blueprint(shortener)

    return app
