from app_package import db

connection_table = db.Table('relations',
                            db.Column('table1_id', db.Integer, db.ForeignKey('table1.table1_id')),
                            db.Column('table2_id', db.Integer, db.ForeignKey('table2.table2_id'))
                            )


class Table1(db.Model):
    table1_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String)
    table2 = db.relationship("Table2", secondary=connection_table)


class Table2(db.Model):
    table2_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String)
    table1 = db.relationship("Table1", secondary=connection_table)