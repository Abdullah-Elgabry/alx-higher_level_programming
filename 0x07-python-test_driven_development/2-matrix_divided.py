#!/usr/bin/python3
"""this is for the divide func."""


def matrix_divided(matrix, div):
    """ths func will be as a num divider.
    Args:
        matrix: [num].
        div: the num will div by
    Returns:
        list: matrix .
    Raises:
        TypeError: will raise in case if the num not int or float.
        TypeError: will raise in case if the size !=.
        TypeError: will raise in case if not int.
        ZeroDivisionError: in zero inpust case.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
