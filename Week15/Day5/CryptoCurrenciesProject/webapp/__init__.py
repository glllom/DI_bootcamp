from flask import Flask
from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

cripto_app = Flask(__name__)
cripto_app.config.from_object(Config)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(cripto_app)

db = SQLAlchemy(cripto_app)
migrate = Migrate(cripto_app, db)

from webapp import routes, models

db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
