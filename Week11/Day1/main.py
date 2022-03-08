import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/sayBye/<name>')
def say_bye(name):
    return f'''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, {name.title()}!</h1>
        <h1>thank!</h1>
    </body>
</html>'''


users = ['Sam', 'Frodo', 'Gymly', 'Boromir']


@app.route('/blog')
def wellcome():
    return f'''
            <html>
                <head>
                    <title>Blog</title>
                </head>
                <body>
                    <h1>Hello, {(user for user in users)}!</h1>
                </body>
            </html>'''


if __name__ == "__main__":
    app.run(debug=True, port=5000)
