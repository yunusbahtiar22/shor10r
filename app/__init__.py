import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    # instanciate the app
    app = Flask(__name__)

    # app configurations
    app.config.from_object('app.config.Config')

    # setup extensions
    db.init_app(app)

    #app.shell_context_processor({"app": app, "db": db})

    return app

def new_func():
    app_settings = os.getenv('APP_SETTINGS')
    return app_settings

