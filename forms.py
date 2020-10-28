from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


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


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=5)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class PostForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    condition = StringField('Condition', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    submit = SubmitField('Post Book')
    

class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')