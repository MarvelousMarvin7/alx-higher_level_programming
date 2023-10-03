#!/usr/bin/python3
def print_last_digit(number):
    """print last digit of a number"""
    number = abs(number) % 10
    print(number, end="")
    return (number)
