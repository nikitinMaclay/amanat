import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class UserProduct(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'user_products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    creator_id = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    product_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    track_number = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    status_in_system = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=True)
    status_china = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    status_kaz = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    status_completed = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    status_archive = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)

