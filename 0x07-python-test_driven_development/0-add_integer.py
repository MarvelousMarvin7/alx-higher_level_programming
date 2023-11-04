#!/usr/bin/python3
''' Function that adds two integers '''


def add_integer(a, b=98):
    """
    Add two integers

    Args:
    a : first integer
    b : integer assigned to 98

    Returns:
    Sum of a plus b

    Raise:
    type error if a and b are not int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a + b)
