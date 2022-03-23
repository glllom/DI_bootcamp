import os

basedir = os.path.abspath(os.path.dirname(__file__))  # Try to avoid hardcoding paths, use os


class Config:
	SECRET_KEY = "kjdsfbnlkvjbhrlkj"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = True
