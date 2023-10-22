#!/usr/bin/python3
""" A module that defines a DataBase storage type """
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """ A class the dsfines a DataBase storage type """
    __engine = None
    __session = None

    def __init__(self):
        _user = os.environ.get('HBNB_MYSQL_USER')
        _passwd = os.environ.get('HBNB_MYSQL_PWD')
        _host = os.environ.get('HBNB_MYSQL_HOST')
        _db = os.environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f"mysql+mysqldb://{_user}:{_passwd}@{_host}/{_db}",
            pool_pre_ping=True
                )

        env = os.environ.get('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query a database session (seld.__session) """
        if cls:
            result = self.__session.query(cls).all()
        else:
            result = self.__session.query(State).all()
            result.extend(self.__session.query(City).all())
            result.extend(self.__session.query(User).all())
            result.extend(self.__session.query(Place).all())
            result.extend(self.__session.query(Review).all())
            result.extend(self.__session.query(Amenity).all())

        return {f"{type(obj).__name__}.{obj.id}": obj for obj in result}

    def new(self, obj):
        """ Add obj to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes to current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from the current database session if ! None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database
            Creates the current database session(self.__session)
                from self.__engine
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False
            )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ call remove() method on the private session attribute
            (self.__session) tips or close()
            on the class Session tips
        """
        self.__session.close()
