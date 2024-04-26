#!/usr/bin/python3
"""this module will return the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """this function will search for the peak in the list"""

    if list_of_integers is None or list_of_integers == []:
        return None
    min = 0
    peak = len(list_of_integers)
    mid = ((peak - min) // 2) + min
    mid = int(mid)
    if peak == 1:
        return list_of_integers[0]
    if peak == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])