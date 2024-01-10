#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    
    strom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dig = 0
    for r in range(len(roman_string)):
        if r > 0 and strom[roman_string[r]] > strom[roman_string[r - 1]]:
            dig += strom[roman_string[r]] - 2 * strom[roman_string[r - 1]]
        else:
            dig += strom[roman_string[r]]
    return (dig)
