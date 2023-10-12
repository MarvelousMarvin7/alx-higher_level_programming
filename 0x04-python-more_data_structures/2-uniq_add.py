#!/usr/bin/python3
"""adds all unique integers in a list"""


def uniq_add(my_list=[]):
    uniql = set(my_list)
    add = sum(uniql)
    return add
