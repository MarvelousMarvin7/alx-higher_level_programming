#!/usr/bin/python3
"""division of matrix"""


def matrix_divided(matrix, div):
    """
    A function that divides all element of a matrix
    Args:
    matrix : matrix containing elements to divide
    div : the divident of matrix

    Return:
    Division of elements in matrix

    Raise:
    TypeError
    if matrix is not list of list of integers and floats,
    if matrix is not same size,
    if div is 0
    """

    prompt = 'matrix must be a matrix (list of lists) of integers/floats'
    prompt_2 = 'Each row of the matrix must have the same size'
    prompt_3 = 'div must be a number'
    length = len(matrix)
    
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(prompt)
    if length == 0:
        raise TypeError(prompt)
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(prompt)
    if not isinstance(div, (int, float, None)):
        raise TypeError(prompt3)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for i in range(length):
        if len(matrix[i]) is not len(matrix[0]):
            raise TypeError(prompt_2)

    # new matrix

    new_matrix = []
    for i in range(length):
        new_matrix.append([])

        for element in matrix[i]:
            if not isinstance(element, (int, float)):
                raise TypeError(prompt)
            else:
                new_matrix[i].append(round(element / div, 2))

    return new_matrix
