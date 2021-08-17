from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import Email
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='User name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
