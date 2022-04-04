from flask import Flask, render_template
import filter
app = Flask(__name__)

app.jinja_env.filters["sum_list"] = filter.sum_list


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", num=[1,2,3,4])


if __name__ == '__main__':
    app.run()
