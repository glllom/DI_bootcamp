import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = 'secret-key-goes-here'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
