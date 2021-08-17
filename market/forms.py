from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='User name:')
    email_address = StringField(label='Email address:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')
