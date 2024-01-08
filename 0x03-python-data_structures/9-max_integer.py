#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    cpy_lst = my_list.copy()
    cpy_lst.sort()
    return cpy_lst[-1]
