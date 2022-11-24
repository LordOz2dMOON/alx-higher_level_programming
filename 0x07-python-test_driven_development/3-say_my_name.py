#!/usr/bin/python3
"""Defines a function that prints a persons full name"""

def say_my_name(first_name, last_name=""):
    """function that prints full name as string"""

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    message = print(f"My name is {first_name} {last_name}")
    return message


