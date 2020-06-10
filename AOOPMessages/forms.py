from flask_wtf import FlaskForm
from wtforms import Form,TextField, TextAreaField, validators, StringField, PasswordField


class LoginForm(FlaskForm):
    email = StringField('email', validators=[validators.required()])
    password = StringField('password', validators=[validators.required()])

class SignupForm(FlaskForm):
    email = StringField('email', validators=[validators.required()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm',
                           message='Passwords must match')
        ])
    confirm = PasswordField('Repeat Password')