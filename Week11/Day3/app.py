import flask

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    code = "<h1>Hello, World</h1>"
    return code


@app.route('/blog')
def greeting_users():
    users = ['Asimov', 'Bradbury']
    return flask.render_template("homepage.html", users=users)


@app.route('/blog/articles')
def show_articles():
    articles = [{'title': 'Foundation', 'author': 'Asimov', 'year': 1951},
                {'title': 'Fahrenheit 451', 'author': 'Bradbury', 'year': 1953}]
    return flask.render_template("articles.html", articles=articles)


if __name__ == '__main__':
    app.run()
