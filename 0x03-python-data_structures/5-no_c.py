#!/usr/bin/python3
"""Remove Cc from a  string"""


def no_c(my_string):
    new_string = ""
    for s in my_string:
        if s.lower() != 'c' and s.upper() != 'C':
            new_string += s
    return new_string
