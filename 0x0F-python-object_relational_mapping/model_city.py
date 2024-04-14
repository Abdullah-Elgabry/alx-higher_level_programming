#!/usr/bin/python3
"""
this class contains the class definition of a City
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): class table name.
        id (int): class id.
        name (str): class name.
        state_id (int): city state anchor
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
