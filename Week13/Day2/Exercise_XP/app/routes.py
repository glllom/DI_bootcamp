import json
import flask
from app import flask_app    # app.app is package_name.variable_name
from models import Users


@flask_app.route("/")
def index():
    return 'sfsfsdfsdf'


def populate():
    with open('users.json', 'r') as f:
        users = json.load(f)
    for user in users:
        new_user = Users(name=user['name'],
                         street=user['address']['street'],
                         city=user['address']['city'],
                         zipcode=user['address']['zipcode'])


populate()

