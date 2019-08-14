from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=5,max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password =PasswordField('confirm Password',validators=[DataRequired(),Length(min=6,max=20), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login') 