import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '15646cxv(gdfy57@j4654654^$5464'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'cripto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    DATABASE = "/cripto.db"
