#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    """ Amenity class to store amenity information """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # Define Many-To-Many relationship with Place
    place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")
