import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1564659465465165465465465465465464'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'cripto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
