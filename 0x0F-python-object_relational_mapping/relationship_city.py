#!/usr/bin/python3
"""
City class script
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): class table name.
        id (int): class ID.
        name (str): class name.
        state_id (int): anchor to the state.

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
