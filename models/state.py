#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        def __init__(self, *args, **kwargs):
            """initializes state"""
            super().__init__(*args, **kwargs)

        @property
        def cities(self):
            """return a list of city instances with state_id = current"""
            all_instances = models.storage.all(City)
            query = []
            for key, value in all_instances.items():
                if getattr(value, 'state_id') == self.id:
                    query.append(value)
            return query
