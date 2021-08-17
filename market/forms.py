from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import Email
from wtforms.validators import DataRequired
from market.models import User
from wtforms.validators import ValidationError


class RegisterForm(FlaskForm):

    # serve per controllare che non esista a db l'utente che sto per creare
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exits! Please try a different username.')

    # serve per evitare di creare uno username con stesso email address
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Please try a different email address.')

    username = StringField(label='User name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')
