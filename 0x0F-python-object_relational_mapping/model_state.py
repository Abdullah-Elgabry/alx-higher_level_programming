#!/usr/bin/python3
"""
this script contains the class definition of a State..
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): table name
        id (int): state ID
        name (str):class state name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
