from flask_wtf import FlaskForm
from wtforms import Form,TextField, TextAreaField, validators, StringField, PasswordField, HiddenField
from wtforms.widgets import TextArea


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


class MessageForm(FlaskForm):
    class Meta:
        csrf = False
    title = StringField('title', validators=[validators.required()])
    author_id = HiddenField('author_id')
    to =  StringField('to', validators=[validators.required()])
    body = StringField('body', validators=[validators.required()],widget=TextArea())