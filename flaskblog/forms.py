from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField, BooleanField


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=2, max=50)])
    email = StringField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField("Sign Up")
    
    
class LoginForm(FlaskForm):
    email = StringField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign Up")
