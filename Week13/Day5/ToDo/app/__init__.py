from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

flask_app = Flask(__name__, static_folder='static')
flask_app.config.from_object(Config)


db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)


from app import routes, models
db.create_all()

