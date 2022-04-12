from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app.config import Config

db = SQLAlchemy()


def create_app():
    cards_app = Flask(__name__)
    cards_app.config.from_object(Config)
    db.init_app(cards_app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(cards_app)

    from app.auth.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.auth.auth import auth as auth_blueprint
    cards_app.register_blueprint(auth_blueprint)

    from app.main.main import main as main_blueprint
    cards_app.register_blueprint(main_blueprint)

    return cards_app
