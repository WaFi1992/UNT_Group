from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=5), validateEmail()])
    
    def validateEmail(form, field):
        if '@unt.edu' or '@my.unt.edu' not in field.data:
            raise ValidationError('Email must be from a UNT address')
