#!/usr/bin/python3
"""this module represinting pascal_triangle func"""


def pascal_triangle(n):
    """this func will calc the pascal_triangle"""

    if n <= 0:
        return []

    tr_bs = [[1]]
    while len(tr_bs) != n:
        tri = tr_bs[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tr_bs.append(tmp)
    return tr_bs
