#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='delete')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
