#!/usr/bin/python3
"""
State class updating.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): class table name
        id (int): class (state ID)
        name (str): class state (name)
        cities (:obj:`City`): anchor to city (REL)

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
