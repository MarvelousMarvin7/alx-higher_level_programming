#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after characters
    . ? :

    Arg:
    Text : text to indent
    """
    new_line = ""
    last = " "

    if text is "":
        print(new_line, end="")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i is last and i is " ":
            last = i
            continue
        if (last is "." or last is "?" or last is ":") and i is " ":
            last = i
            continue
        if i is "." or i is "?" or i is ":":
            new_line += i + "\n" + "\n"
            last = i
        else:
            new_line += i
            last = i
    print(new_line.rstrip(' '), end="")
