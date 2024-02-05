#!/usr/bin/python3
'''this is for base geometry class.'''


class BaseGeometry:
    '''class to cotians calculation of the shapes'''
    def area(self):
        '''this will get the area of the shape.'''
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        '''this func will checks the val'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))