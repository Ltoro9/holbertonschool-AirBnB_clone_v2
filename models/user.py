#!/usr/bin/python3
"""comment"""


ffrom sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    '''
        User class
    '''
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Define relationship with Place
    places = relationship("Place", cascade="all, delete", back_populates="user")
