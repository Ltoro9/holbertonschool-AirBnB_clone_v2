#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class to store amenity information"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    places = relationship("Place", secondary="place_amenity", back_populates="amenities")

    place_amenity = Table('place_amenity', BaseModel.metadata,
                          Column('place_id', String(60), ForeignKey('place.id'), primary_key=True),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
                          )
