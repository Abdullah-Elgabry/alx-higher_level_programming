#!/usr/bin/python3
"""this module represinting student class"""


class Student:
    """this class will contain stdudent main functions"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this will get the dict back with all stdunt info."""
        return self.__dict__
