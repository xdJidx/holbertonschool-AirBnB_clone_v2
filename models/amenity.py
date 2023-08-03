#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Table, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


# Define the association table for the Many-To-Many relationship
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Amenity(BaseModel, Base):
    """Amenity class to store amenities for HBNB project"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # Define the Many-To-Many relationship with Place
    place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")
