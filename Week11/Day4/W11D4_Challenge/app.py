from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<color>')
def show_color(color):
    return render_template('color.html', color=color)


if __name__ == '__main__':
    app.run()
