import flask
from app import flask_app


@flask_app.errorhandler(404)
def error_404(error):
    return flask.render_template('errors/404_error.html'), 404
