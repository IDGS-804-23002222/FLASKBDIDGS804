import os

from sqlalchemy import create_engine


class Config(object):
    SECRET_KEY = 'Clave_Secreta'
    SESSION_COOKIE_SECURE = False



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:karlamtz233@localhost/bdidgs804'
    SQLALCHEMY_TRACK_MODIFICATIONS = False