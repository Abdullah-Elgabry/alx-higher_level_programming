#!/usr/bin/python3
"""this module represinting py script to reads file"""


from sys import stdin

status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

list_sz = x = 0


def printer():
    """printer func will acts as cond"""
    print(f'File size: {list_sz}')
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print('{:s}: {:d}'.format(k, v))


try:
    for line in stdin:
        splitted_line = line.split()
        if len(splitted_line) >= 2:
            status = splitted_line[-2]
            list_sz += int(splitted_line[-1])
            if status in status_codes:
                status_codes[status] += 1
        x += 1

        if x % 10 == 0:
            printer()
    printer()
except KeyboardInterrupt as e:
    printer()
