from flask import Flask
from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    cripto_app = Flask(__name__)
    cripto_app.config.from_object(Config)
    db.init_app(cripto_app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(cripto_app)

    from webapp.auth.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from webapp.auth.routes import auth as auth_blueprint
    cripto_app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return cripto_app
# from webapp import routes, models
# db.create_all()
