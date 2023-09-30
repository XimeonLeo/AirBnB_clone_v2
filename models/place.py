#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
import os
storage_type = os.environ.get("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False)
                        )


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
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False,
                                 backref='place_amenities')
    else:
        city_id = ""
        user_id = "" 
        name = "" 
        description = ""
        number_rooms = 0
        number_bathrooms = 0 
        max_guest = 0     
        price_by_night = 0 
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns A list of review associated with
                this place
            """
            from models import storage, Review
            reviews = []
            for review in storage.all(Review).values():
                if review.places_id == self.id:
                    reviews.append(review)
            return review

        @property
        def amenities(self):
            """Returns A list of amenities associated with
                this place
            """
            from models import Amenity
            amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity._id == self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, amenity_obj):
            """Handles append method for adding Amenity.id
                to the attribute amenity_ids
            """
            if amenity_obj:
                if isinstance(amenity_obj, Amenity):
                    if amenity_obj.id not in self.amenity_ids:
                        self.amenity_ids.append(amenity_obj.id)
