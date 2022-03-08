from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    GameOfLife(25, 20)
    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter_of_generations > 0:
        game.form_new_generation()
    game.counter_of_generations += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
