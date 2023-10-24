#!/usr/bin/python3
"""Clear a string at a position"""


def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        return (str[:n] + str[n+1:])
