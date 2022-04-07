from flask import Flask
from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

cripto_app = Flask(__name__)
cripto_app.config.from_object(Config)

db = SQLAlchemy(cripto_app)
migrate = Migrate(cripto_app, db)
from webapp import routes, models

db.create_all()
