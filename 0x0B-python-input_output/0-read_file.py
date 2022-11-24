#!/usr/bin/python3
"""This is a module that creates a function to read a file"""

def read_file(filename=""):
    """function that reads filename and prints it to stdout"""
    with open(filename, encoding='utf-8') as file:
        contents = file.read()

    print(contents, end='')
