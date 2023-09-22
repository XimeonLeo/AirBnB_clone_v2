#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from os import getenv
from sqlalchemy.orm import sessionmaker
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """ New storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Public instance method that links engine and db """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)

    def all(self, cls=None):
        """ Query current db session of specified class """
        class_list = [Amenity, City, Place, Review, State, User]

        if self.cls is None:
            for i in range(0, len(class_list) - 1):
                self.__session.query(eval(class_list[i])).filter_by().all()
