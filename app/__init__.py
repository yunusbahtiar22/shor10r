import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    # instanciate the app
    app = Flask(__name__)

    # pull the config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # setup extensions
    db.init_app(app)

    return app

