#!/usr/bin/python3
"""Find all multiples of 2"""


def divisible_by_2(my_list=[]):
    new_list = []
    length = range(len(my_list))
    for i in length:
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
