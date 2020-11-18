from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from bookapp.models import User
import requests
from bs4 import BeautifulSoup
import re


class RegistrationForm(FlaskForm):
    
    def validateEmail(form, field):
        if 'unt.edu' not in field.data:
            raise ValidationError('Email must be from a UNT address')


    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(check_deliverability=True), validateEmail])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField('Confirm Password',
                             validators=[DataRequired(), Length(min=5), EqualTo('password')])
    payment_profile = StringField('Payment Profile',
                           validators=[Length(min=2, max=25)])
    major = StringField('Major',
                           validators=[Length(min=2, max=20)])
    submit = SubmitField('Sign up')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account with that email already exists')               


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=5)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class PostForm(FlaskForm):
    #isbn = StringField('ISBN', validators=[DataRequired()])

    #isbn = 9781947556744

    
   
    #data required from user

    #title = StringField('Title', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    #description = TextAreaField('Description', validators=[DataRequired()])
    condition = StringField('Condition', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])

    submit = SubmitField('Post Book')
    

class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')