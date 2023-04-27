from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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
