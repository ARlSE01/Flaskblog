from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class signup(FlaskForm):
    username= StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired(),Length(min=5)])
    confirm_password=PasswordField('confirm-password',validators=[DataRequired(),Length(min=5),EqualTo('password')])
    submit=SubmitField('signup')


class login(FlaskForm):
    username= StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField('password',validators=[DataRequired(),Length(min=5)])
    remember=BooleanField('Remember Me')
    login=SubmitField('login')