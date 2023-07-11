from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    product_name = StringField('Название продукта')
    product_description = StringField('Описание продукта')
    product_img = FileField()
    submit = SubmitField('Добавить товар')
