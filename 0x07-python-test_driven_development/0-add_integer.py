#!/usr/bin/python3
"""Addition of 2 integers"""


def add_integer(a, b=98):
    """Add 2 integers together

    Args:
    a : first integer
    b : Second integer

    Raise: TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
