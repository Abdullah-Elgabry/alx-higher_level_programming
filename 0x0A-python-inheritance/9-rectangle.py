#!/usr/bin/python3
'''this for the rectangle class'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''this is class inherit from basegeometry claass for rect info'''
    def __init__(self, width, height):
        '''this is the func Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''this func will return the rect area'''
        return self.__width * self.__height

    def __str__(self):
        '''this will ret the rect dimensions'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
