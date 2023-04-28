from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from storedatas.models import User

'''
If you got Emai() error:
  You should to --> pip install wtforms[email]
'''


class NewUserFrom(FlaskForm):
    username = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Repeat your password', validators=[DataRequired(), EqualTo('password', message='Wrong confirm')])

    submit = SubmitField('Register')

    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('Name already use')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already use')


class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Still Logged')

    submit = SubmitField('Login')
