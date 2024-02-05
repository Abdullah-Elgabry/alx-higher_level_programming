#!/usr/bin/python3
'''this is for square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''this inherit class id for square data'''
    def __init__(self, size):
        '''this is the func Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''this func will get the area square'''
        return self.__size ** 2
