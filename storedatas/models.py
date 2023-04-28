from storedatas import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(15), unique=True, nullable=False)
    lastname = db.Column(db.String(15), unique=True, nullable=False)
    date = db.Column(db.String(15))

    def __repr__(self):
        return f'Employee({self.firstname}, {self.lastname}, {self.date})'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f'User({self.name}, {self.email}, {self.password})'
