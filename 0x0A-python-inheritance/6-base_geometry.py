#!/usr/bin/python3
'''this is for base geometry class.'''


class BaseGeometry:
    '''class to cotians calculation of the shapes'''
    def area(self):
        '''this will get the area of the shape.'''
        raise Exception('area() is not implemented')
