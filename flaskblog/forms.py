from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField, BooleanField
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=2, max=50)])
    email = StringField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField("Sign Up")
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise validators.ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise validators.ValidationError('That email is taken. Please choose a different one.')
    
    
class LoginForm(FlaskForm):
    email = StringField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign Up")
