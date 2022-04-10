from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app_package.config import Config


test_app = Flask(__name__)
test_app.config.from_object(Config)
db = SQLAlchemy(test_app)
migrate = Migrate(test_app, db)
from app_package import models
db.create_all()


@test_app.route('/')
def hello_world():
    return 'Hello World!'

