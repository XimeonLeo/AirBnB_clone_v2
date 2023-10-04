#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Defines a class Amenity """
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128),
                      nullable=False)
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates="amenities")
    else:
        name = ""
