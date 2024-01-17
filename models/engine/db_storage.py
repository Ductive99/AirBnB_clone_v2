#!/usr/bin/python3
""" This Module defines a class to manage database storage """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """"""
    __engine = None
    __session = None
    __classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):
        """ Class that creates the engine for MySQL """
        ms_usr = getenv('HBNB_MYSQL_USER')
        ms_pwd = getenv('HBNB_MYSQL_PWD')
        ms_host = getenv('HBNB_MYSQL_HOST')
        ms_db = getenv('HBNB_MYSQL_DB')
        ms_env = getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(ms_usr, ms_pwd, ms_host, ms_db),
                                      pool_pre_ping=True)

        if ms_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary

        key = <class-name>.<object-id>
        value = object
        """
        result_dict = {}

        if cls:
            for row in self.__session.query(cls).all():
                key = cls.__class__.__name__ + '.' + row.id
                result_dict[key] = row
        else:
            for k, v in self.__classes:
                for row in self.__session.query(v):
                    key = row.__class__.__name__ + '.' + row.id
                    result_dict[key] = row
        return result_dict

    def new(self, obj):
        """ Adds the object to the current DB session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current DB session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the obj from the current DB session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database
        Creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """ Closes the storage engine """
        self.__session.close()
