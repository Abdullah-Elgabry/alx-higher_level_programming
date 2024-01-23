#!/usr/bin/python3
"""Defining the magic class."""

import math


class MagicClass:
    """definig the class."""

    def __init__(self, radius=0):
        """Class INIT.
        Arg:
            radius (float or int): The Class rad.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """get circle area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """get circle circum."""
        return (2 * math.pi * self.__radius)
