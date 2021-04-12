import os

class Config:
    """ Base Configuration """
    USERNAME = 'admin'
    PASSWORD = 'password'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///url.db"
