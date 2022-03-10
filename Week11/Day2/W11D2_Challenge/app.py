import flask
import markdown
app = flask.Flask(__name__)


@app.route('/')
@app.route('/lesson')
def in_this_chapter():
    with open('lesson1/in-this-chapter.md', 'r') as f:
        content = markdown.markdown(f.read(), extensions=["fenced_code"])
    return flask.render_template('di_platform.html', content=content)


@app.route('/exercises')
def exercises():
    with open('lesson1/exercises.md', 'r') as f:
        content = markdown.markdown(f.read(), extensions=["fenced_code"])
    return flask.render_template('di_platform.html', content=content)


if __name__ == '__main__':
    app.run()
