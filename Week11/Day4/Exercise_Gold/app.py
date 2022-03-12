from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<int:number>')
def fibonacci(number):
    sequence = []
    for i in range(number):
        sequence.append(i)
    return render_template('fibonacci.html', sequence=sequence)


if __name__ == '__main__':
    app.run()