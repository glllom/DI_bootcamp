from flask import Flask
import json
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

from app import routes

flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'robots.db')
flask_app.secret_key = 'dfshdjkfghsdlkghiudfgdfgjk'

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)
