import flask
import flask_migrate
import flask_sqlalchemy

from app.config import Config

flask_app = flask.Flask(__name__)  # Remember: __name__ is the name of the file where the code is written

flask_app.config.from_object(Config)

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import models

db.create_all()
