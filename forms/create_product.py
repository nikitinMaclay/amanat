from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class CreateProductForm(FlaskForm):
    product_name = StringField('Название продукта', validators=[DataRequired()])
    track_number = PasswordField('Трек номер', validators=[DataRequired()])
    submit = SubmitField('Добавить товар')
