from flask import Flask
from app.films.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

films_app = Flask(__name__)
films_app.config.from_object(Config)


db = SQLAlchemy(films_app)
migrate = Migrate(films_app, db)
from app.films import routes, models
db.create_all()
