import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Status(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'status'

    status_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    status_naming = sqlalchemy.Column(sqlalchemy.String)
    user_product = relationship("UserProduct")