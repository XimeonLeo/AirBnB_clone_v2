#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import os
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel):
    if storage_type == "db":
        pass
    else:
        name = ""
