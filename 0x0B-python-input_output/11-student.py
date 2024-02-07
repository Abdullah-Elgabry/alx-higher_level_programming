#!/usr/bin/python3
"""this module for student class"""

class Student:
    """this class represent student functions"""
    def __init__(self, first_name, last_name, age):
        '''constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        this will get the dictionary back with all
        student info
        """
        try:
            for plt in attrs:
                if type(plt) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """
        this func just replace the value
        """
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v