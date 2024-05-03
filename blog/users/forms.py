from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from email_validator import validate_email, EmailNotValidError
from blog.models.models import User


class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    username = StringField("username", validators=[DataRequired(), Length(min=2, max=20)],
                           render_kw={'placeholder': 'Username'})
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)],
                             render_kw={'placeholder': 'Password'})
    password2 = PasswordField("Confirm password",
                              validators=[DataRequired(), Length(min=6), EqualTo('password')],
                              render_kw={'placeholder': 'Confirm password'})
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        try:
            v = validate_email(email.data, check_deliverability=False)
            email.data = v.normalized
        except EmailNotValidError as e:
            raise ValidationError(str(e))
        u = User.query.filter_by(email=email.data).first()
        if u:
            raise ValidationError('That email is taken. Please choose a different one.')

    def validate_username(self, username):
        u = User.query.filter_by(username=username.data).first()
        if u:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    # email = EmailField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')

    # def validate_email(self, email):
    #     if email.data != current_user.email:
    #         u = User.query.filter_by(email=email.data).first()
    #         if u:
    #             raise ValidationError('That email is taken. Please choose a different one.')

    def validate_username(self, username):
        if username.data != current_user.username:
            u = User.query.filter_by(username=username.data).first()
            if u:
                raise ValidationError('That username is taken. Please choose a different one.')
