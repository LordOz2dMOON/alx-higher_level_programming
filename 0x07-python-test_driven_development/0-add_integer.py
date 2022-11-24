#!/usr/bin/python3
"""This is a module that contains a function that adds two numbers"""

def add_integer(a, b=98):
    """function add_integer(a, b) adds two integers and returns the sum"""

    if not type(a) is int or float:
        raise TypeError("a must be an integer")
    if not type(b) is int or float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
