#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    dg = 0
    sum = 0

    roman_dg = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(roman_string):
        dg = roman_dg[i]
        sum += dg if sum < dg * 5 else -dg
    return sum
