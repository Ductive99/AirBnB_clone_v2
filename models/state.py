#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import environ


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == "db":
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """ Getter method
            Returns a list of City instances with state_id == State.id
            """
            from models import storage

            city_list = []
            for val in storage.all(City).values():
                if val.state_id == self.id:
                    city_list.append(val)

            return city_list
