#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name
            __tablename__:
                private attribute holding file name
            name:
                sqlalchemy.String, name of cities
            state_is:
                sqlachemy.String, id for the state where city is
    """
    __tablename__ = "ciries"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                        nullable=False, 
                        ForeignKey('state_id'))
