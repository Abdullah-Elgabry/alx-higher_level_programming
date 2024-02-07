#!/usr/bin/python3
"""this module represinting student class"""

class Student:
    """this class will contain stdudent main functions"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this will get the dict back with all stdunt info with conditions."""

        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """this func just replc the values"""

        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value