#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    storage_type = os.environ.get('HBNB_TYPE_STORAGE')

    if storage_type == "db":
        """ Using DBStorage """
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete")
    else:
        name = ''

        @property
        def cities(self):
            """ Returns the list of City instance where
                state_id is the current State.id

                Using FileStorage
            """
            from models import storage
            like_cities = []
            """ for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities """

            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    like_cities.append(city)
            return like_cities
