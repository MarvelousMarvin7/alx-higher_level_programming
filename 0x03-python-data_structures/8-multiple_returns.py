#!/usr/bin/python3
"""Return lenght of string and first character"""


def multiple_returns(sentence):
    length = len(sentence)
    firstchar = sentence[0]
    if length == 0:
        return (0, None)
    else:
        return (length, firstchar)
