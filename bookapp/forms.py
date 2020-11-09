from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from bookapp.models import User

import requests
from bs4 import BeautifulSoup
import re

#pass URL into scrape function
def scrape(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    #find elements
    imgCover = soup.find(id='coverImage')
    title = soup.find(id='describe-isbn-title')
    publisher = soup.find(itemprop='publisher')
    author = soup.find(itemprop='author')


class RegistrationForm(FlaskForm):
    
    def validateEmailDomain(form, field):
        if 'unt.edu' not in field.data:
            raise ValidationError('Email must be from a UNT address')

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(check_deliverability=True), validateEmailDomain])
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

    isbn = 9781947556744

    #(scraping) insert isbn into url to navigate to page with book info
    url = f"https://www.bookfinder.com/search/?author=&title=&lang=en&isbn{str(isbn)}&new_used=*&destination=us&currency=USD&mode=basic&st=sr&ac=qr"
    
    

    #scraping
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #(scraping) find elements
    #might have to take another look at how to retrieve the img
    imgCover = soup.find(id='coverImage')
    
    #find title in between brackets
    title = soup.find(id='describe-isbn-title')
    #xTitle = re.search(r">(.*)<", title.prettify())
    

    publisher = soup.find(itemprop='publisher')
    author = soup.find(itemprop='author')

    #data required from user
    condition = StringField('Condition', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    submit = SubmitField('Post Book')
    

class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')