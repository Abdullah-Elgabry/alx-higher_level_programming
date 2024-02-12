#!/usr/bin/python3
'''this is for implementing the square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class representing a square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize the square.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''this func will get all information for the square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''the square size .'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''this func will re org the sq size  with x and y.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''this func will re org the sq size by the number.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''this func will return the info in {}.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
