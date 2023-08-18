#!/usr/bin/python3
"""This module defines the database storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }


class DBStorage:
    """
    Creates database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Start
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, database),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Perf query on current database
        Returns:
            Dict with all objects accroding to cls args
            Or everything if no args
        """
        objects_dict = {}
        if cls != '':
            objects = self.__session.query(cls)
        else:
            objects = self.__session.query(Amenity)
            objects += self.__session.query(City)
            objects += self.__session.query(Place)
            objects += self.__session.query(User)
            objects += self.__session.query(Review)
            objects += self.__session.query(State)
        return {"{}.{}".format(obj.__class__.__name__, obj.id):
                obj for obj in objects}

    def new(self, obj):
        """
        Adds objects to curretn db session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Commit all changes in db after changings
        """
        self.__session = Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Call
        """
        self.__session.close()
