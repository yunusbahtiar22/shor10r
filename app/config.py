import os


class Config:
    """ Base Configuration """
    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = 'password'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///url.db"
