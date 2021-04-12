import os

class Config:
    USERNAME = "admin"
    PASSWORD = "password"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABSE_URL")
