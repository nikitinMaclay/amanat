from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SearchField
from wtforms.validators import DataRequired


class SearchingForm(FlaskForm):
    search_field = StringField('Поиск', validators=[DataRequired()])
    submit = SubmitField()
