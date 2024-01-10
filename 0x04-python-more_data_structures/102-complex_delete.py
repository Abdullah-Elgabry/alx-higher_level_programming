#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for my_key, my_value in list(a_dictionary.items()):
        if my_value == value:
            del a_dictionary[my_key]
    return a_dictionary
