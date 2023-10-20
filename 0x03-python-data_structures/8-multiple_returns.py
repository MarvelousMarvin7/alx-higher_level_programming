#!/usr/bin/python3
"""Return lenght of string and first character"""


def multiple_returns(sentence):
    tupl = ()
    length = len(sentence)
    if length == 0:
        tupl = 0, "None"
    else:
        tupl = length, sentence[0]

    return tupl
