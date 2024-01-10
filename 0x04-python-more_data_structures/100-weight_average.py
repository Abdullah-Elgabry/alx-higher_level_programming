#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(st * nd for st, nd in my_list) / sum(nd for st, nd in my_list))
