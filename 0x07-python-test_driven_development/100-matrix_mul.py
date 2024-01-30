#!/usr/bin/python3
"""this Module is for multiply func."""


def matrix_mul(mbx, mtx):
    """this func will multiply 2 [].
    Args:
        mbx: 1st [].
        mtx: 2nd[].
    Returns:
        matrix: the mul [] is the result
    Raises:
        TypeError: error will raise in case xx [2].
        TypeError: error will raise in case xx [2] [].
        ValueError: error will raise in case [2]or matrics.
        TypeError: error will raise in case [2] is n/a.
        TypeError: error will raise in case [2] is x rect.
        ValueError: error will raise in case [2] in error in mul.
    """

    if not isinstance(mbx, list):
        raise TypeError("mbx must be a list")
    if not isinstance(mtx, list):
        raise TypeError("mtx must be a list")
    nast = False
    nand = False
    nakl = False
    nankl = False
    nanum = False
    nanmun = False
    for row in mbx:
        if not isinstance(row, list):
            raise TypeError("mbx must be a list of lists")
        if len(row) != len(mbx[0]):
            nakl = True
        for num in row:
            if not isinstance(num, (int, float)):
                nanum = True

    for row in mtx:
        if not isinstance(row, list):
            raise TypeError("mtx must be a list of lists")
        if len(row) != len(mtx[0]):
            nankl = True
        for num in row:
            if not isinstance(num, (int, float)):
                nanmun = True

    if len(mbx) == 0 or (len(mbx) == 1 and len(mbx[0]) == 0):
        raise ValueError("mbx can't be empty")

    if len(mtx) == 0 or (len(mtx) == 1 and len(mtx[0]) == 0):
        raise ValueError("mtx can't be empty")

    if nanum:
        raise TypeError("m")

    if nanmun:
        raise TypeError("mtx should contain only integers or floats")

    if nakl:
        raise TypeError("each row of mbx must should be of the same size")

    if nankl:
        raise TypeError("each row of mtx must should be of the same size")

    if len(mbx[0]) != len(mtx):
        raise ValueError("mbx and mtx can't be multiplied")

    res = [[] for xl in range(len(mbx))]

    for xl in range(len(mbx)):
        for xm in range(len(mtx[0])):
            c = 0
            for k in range(len(mtx)):
                c += mbx[xl][k] * mtx[k][xm]
            res[xl].append(c)

    return res

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
