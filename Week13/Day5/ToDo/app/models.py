from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    details = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    image = db.relationship("Image", backref='todo', uselist=False)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_task_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def set_task_as_complete(self):
        self.completed = True
        db.session.commit()


class Image(db.Model):
    image_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    url = db.Column(db.String)
    task = db.Column(db.Integer, db.ForeignKey('todo.id'))

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_task_from_db(self):
        db.session.delete(self)
        db.session.commit()