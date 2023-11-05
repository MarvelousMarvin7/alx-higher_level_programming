#!/usr/bin/python3
"""Print Name"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints name

    Args:
    first_name : First name of user
    last_name: Last name of user

    Return: Full name of user

    Raise:
    TypeError:
    first_name must be a string
    last_name must be a string
    """

    prompt = 'first_name must be a string'
    prompt_1 = 'last_name must be a string'

    if not isinstance(first_name, str):
        raise TypeError(prompt)
    if not isinstance(last_name, str):
        raise TypeError(prompt_1)
    print("My name is {} {}".format(first_name, last_name))
