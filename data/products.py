import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Product(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'products'

    product_id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    product_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    product_description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    product_picture_path = sqlalchemy.Column(sqlalchemy.String, nullable=False)
