#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
