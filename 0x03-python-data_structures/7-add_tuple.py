##!/usr/bin/python3
"""Add two tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tup1 = tuple_a + (0, 0)
    tup2 = tuple_b + (0, 0)
    new_tuple = (tup1[0] + tup2[0], tup1[1] + tup2[1])
    return new_tuple
