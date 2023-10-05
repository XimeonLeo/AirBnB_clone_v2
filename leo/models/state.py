#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    storage_type = os.environ.get('HBNB_TYPE_STORAGE')

    if storage_type == db:p
    """ Using DBStorage """
        cities = relationship("City",
                                backref="state",
                                cascade="all, delete")
    else:
        @property
        def cities(self):
            """ Returns the list of City instance where
                state_id is the current State.id

                Using FileStorage
            """
            from models import storage, City

            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
