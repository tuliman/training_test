from app import db
from datetime import date


# first_table user_id, name, middle_name, bornDate, gender
# user_id, education, comment, citizenship

class Person(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    born_date = db.Column(db.Date)
    gender = db.Column(db.String(100))
    addition_info = db.relationship("AdditionPerson", backref='person_start', lazy=True)


class AdditionPerson(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    education = db.Column(db.String(255))
    citizen = db.Column(db.Boolean)
    comment = db.Column(db.Text)
    id = db.Column(db.Integer, db.ForeignKey('person.user_id'),nullable=False)

