from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    phone_num = StringField('Phone Num', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
