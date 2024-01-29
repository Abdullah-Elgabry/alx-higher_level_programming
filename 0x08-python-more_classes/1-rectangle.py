#!/usr/bin/python3
"""
Defining Rectangle class
"""


class Rectangle:
    """Rrectangle class init"""
    def __init__(self, width=0, height=0):
        """set the regt size"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """private instance -> width(getter)"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance -> width(setter)"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance -> height(getter)"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance -> height(getter)"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
