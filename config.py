
import os


class BaseConfig():
    DEBUG = False
    SECRET_KEY = '\xa9\xe5\x91R\xfak\x14\xb5\xf5\x83S\x83\r\x8f=S+7D\xbb\x9d#\x98\x98'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

