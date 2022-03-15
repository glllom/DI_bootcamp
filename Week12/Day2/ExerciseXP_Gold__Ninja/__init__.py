import flask
import random
flask_app = flask.Flask(__name__)  # Remember: __name__ is the name of the file where the code is written


flask_app.config['SECRET_KEY'] = ''.join([chr(random.randint(97, 122)) for _ in range(256)])

# from app import routes

