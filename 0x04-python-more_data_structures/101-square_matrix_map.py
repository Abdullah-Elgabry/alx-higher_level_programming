#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda n: list(map(lambda d: d**2, n)), matrix))
