#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class User(BaseModel, Base):
    """This class defines a user by various attributes
        __tablename__: the name of the table
        email:
            (sqlalchemy.String), the email of ths user
        password:
            (sqlalchemy.String) the password of the user
        first_name:
            (sqlalchemy.String), the users first name
        last_name:
            (sqlalchemy.String), the last name of the user
    """
    __tablename__ = "users"
    email = Column(String(128),
                   nullable=False)
    password = Column(String(128),
                      nullable=False)
    first_name = Column(String(128),
                        nullable=True)
    last_name = Column(String(128),
                       nullable=True)
