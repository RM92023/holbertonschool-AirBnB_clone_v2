#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models
import shlex


class State(BaseModel, Base):
    """
    Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='stats', cascade='all, delete')
    else:
        @property
        def cities(self):
            """return the cities of the current state"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list
