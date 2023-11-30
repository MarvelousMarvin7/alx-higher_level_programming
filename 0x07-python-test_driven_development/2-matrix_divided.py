#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """
    A function that divides all element of a matrix

    Args:
    matrix - matrix values to be divided
    div - the value to divide with

    Raise: TypeError, ZeroDivisionError
    """
    prompt0 = TypeError(
        "matrix must be a matrix (list of lists) of integers/floats"
    )
    prompt1 = TypeError("Each row of the matrix must have the same size")
    prompt2 = TypeError("div must be a number")
    prompt3 = ZeroDivisionError("division by zero")

    new = []

    if not matrix or matrix == [[]] or matrix is None:
        raise prompt0
    if not isinstance(div, (int, float)):
        raise prompt2
    if div == 0:
        raise prompt3

    if matrix[0]:
        length = len(matrix[0])
    else:
        raise prompt1
    for i in range(len(matrix)):
        if len(matrix[i]) != length:
            raise prompt1
        new.append([])
        for a in matrix[i]:
            if isinstance(a, (int, float)):
                new[i].append(round(a / div, 2))
            else:
                raise prompt0
    return new
