#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    cp_lst = my_list.copy()
    cp_lst[idx] = element
    return cp_lst
