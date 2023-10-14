#!/usr/bin/python3
"""convert roman numeral to integer"""


def roman_to_int(roman_string):
    # check if roman_string is not a string or empty
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # create a dictionary for their integer values
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0

    for symbol in roman_string:
        if symbol not in roman_dict:
            return 0
        value = roman_dict[symbol]

        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value

        prev_value = value

    return total
