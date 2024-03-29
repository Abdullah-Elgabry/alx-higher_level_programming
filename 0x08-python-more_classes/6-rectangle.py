#!/usr/bin/python3
"""
Defining Rectangle class
"""


class Rectangle:
    """Rrectangle class init"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Iset the regt size"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """this func will popup msg when del a Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        """private instance -> height(setter)"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to return the rect area"""
        return self.__width * self.__height

    def perimeter(self):
        """function to return the rect  perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """this func will print rect str"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """func aims to reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
