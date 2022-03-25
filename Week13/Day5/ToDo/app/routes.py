import app
from app import flask_app
from flask import render_template, redirect, url_for
from app.forms import AddToDo
from app.models import Todo, Image


@flask_app.route("/", methods=['GET', 'POST'])
def index():
    form = AddToDo()
    tasks = Todo.query.all()
    if form.validate_on_submit():
        new_task = form.task.data
        url = form.url.data
        new_record = Todo(details=new_task)
        new_record.save_task_to_db()
        new_image = Image(url=url, todo=new_record)
        new_image.save_task_to_db()
        return redirect(url_for('index'))
    return render_template('index.html', form=form, tasks=tasks)


@flask_app.route('/complete/<int:todo_id>')
def complete(todo_id):
    record = Todo.query.get(todo_id)
    record.set_task_as_complete()
    return redirect(url_for("index"))


@flask_app.route('/clear_all')
def clear_all():
    Todo.query.delete()
    Image.query.delete()
    app.db.session.commit()
    return redirect(url_for("index"))


@flask_app.route('/remove/<int:todo_id>')
def remove_record(todo_id):
    record = Todo.query.get(todo_id)
    record.image.remove_task_from_db()
    record.remove_task_from_db()
    return redirect(url_for("index"))
