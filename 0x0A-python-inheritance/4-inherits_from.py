#!/usr/bin/python3
'''this is forthe inherits_from func.'''


def inherits_from(obj, a_class):
    '''this func will checks by isinstance if the obj is sub classor not.'''
    return isinstance(obj, a_class) and type(obj) != a_class
