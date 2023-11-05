#!/usr/bin/python3
"""Print A square"""


def print_square(size):
    """
    Print a square with a #

    Args:
    size : size of square

    Return: Nothing

    Raise:
    TypeError : size must be integer
    If size is not an integer.
    If size is a float and is < 0
    ValueError : size must be >= 0

    """
    prompt = 'size must be an integer'
    prompt_1 = 'size must be >= 0'

    if not isinstance(size, int):
        raise TypeError(prompt)
    if type(size) is float and size < 0:
        raise TypeError(prompt)
    if size < 0:
        raise ValueError(prompt_1)

    for i in range(int(size)):
        print("#" * int(size))
