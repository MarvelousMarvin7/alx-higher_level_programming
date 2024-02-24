#!/usr/bin/python3
"""Read a text file"""


def read_file(filename=""):
    """Read from a file

    Args:
    filename = name of file to read from
    """
    with open(filename, 'r', encoding='utf-8') as f:
        f_read = f.read()
        print(f_read, end="")
