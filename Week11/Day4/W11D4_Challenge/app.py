import json

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def homepage():
    return render_template('index.html')


@app.route('/<string:color>')
def show_color(color):

    return render_template('color.html', color=color)


if __name__ == '__main__':
    app.run()
