import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's;kldj;alskjl;aksf9345093458i'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'cards.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
