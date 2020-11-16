from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from bookapp.models import User


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

    def validate_username(self, username):
        if username.data != current_user.username:
        user = User.quert.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different username')      

    def validate_email(self, email):
    email = Email.query.filter_by(email=email.data).first()
       if email:
            raise ValidationError('That email is taken. Please choose a different email.')



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
    
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Request Password Reset')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')    

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField('Confirm Password',
                             validators=[DataRequired(), Length(min=5), EqualTo('password')])
     submit = SubmitField('Reset Password')                    
    
class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')
    
    
class UpdateAccountForm(FlaskForm):
        username = StringField('Username',
                                validator=[DataRequired(), Length(min=2, max=20)])
        email = StringField('Email',
                             validators=[DataRequired(), Email()])
        picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
        submit = SubmitField('Update')