#!/usr/bin/python3
'''this is for the MyList class.'''


class MyList(list):
    '''this is for testing the power of inherit'''
    def print_sorted(self):
        '''this will print [in order]'''
        print(sorted(self))
