#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os
storage_type = os.environ.get("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay
    """
    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(String(60),
                         ForeignKey("cities.id"),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey("users.id"),
                         nullable=False)
        name = Column(String(128),
                      nullable=False)
        description = Column(String(128),
                             nullable=True)
        number_rooms = Column(Integer,
                              default=0,
                              nullable=False)
        number_bathrooms = Column(Integer,
                                  default=0,
                                  nullable=False)
        max_guest = Column(Integer,
                           default=0,
                           nullable=False)
        price_by_night = Column(Integer,
                                default=0,
                                nullable=False)
        latitude = Column(Float,
                          nullable=True)
        longitude = Column(Float,
                           nullable=True)
        amenity_ids = []
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete")
    else:
        @property
        def reviews(self):
            """Returns A list of review associated with this state
            """
            from models import storage, Review
            reviews = []
            for review in storage.all(Review).values():
                if review.places_id == self.id:
                    reviews.append(review)
            return review
