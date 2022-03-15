import flask
"""Exercise 1"""
print(dir(flask))

"""Exercise2"""
app = flask.Flask(__name__)


@app.route('/')
def cv():
    return flask.render_template('cv_1.html', name="Gleb Omarov")


if __name__ == '__main__':
    app.run()