#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan", single_parent=True, passive_deletes=True)

    @property
    def cities(self):
        """ return list of City instances with equal state_id """
        from models import storage
        for k, v in storage.all(City).items():
            if v.state_id == self.id:
                return v
