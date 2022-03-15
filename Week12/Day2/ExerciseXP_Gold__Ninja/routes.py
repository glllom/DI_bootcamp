import flask
from app import flask_app
from forms import AddCity
import cities_app


@flask_app.route('/index')
def index():
    return 'hello'