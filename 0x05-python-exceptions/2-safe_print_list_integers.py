#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    m = 0
    l = 0
    while m < x:
        try:
            print("{:d}".format(my_list[m]), end='')
            l += 1
        except (ValueError, TypeError):
            pass
        m += 1
    print()
    return l
