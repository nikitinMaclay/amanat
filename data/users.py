import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String)
    user_city = sqlalchemy.Column(sqlalchemy.String)
    user_products_relation = relationship("UserProduct")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
