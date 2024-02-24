#!/usr/bin/python3
"""Write to file"""


def write_file(filename="", text=""):
    """Write to file

    Args:
    filename: file to write to
    text: text to write in file
    """
    with open(filename, 'w', encoding = 'utf-8') as f:
        return f.write(text)
