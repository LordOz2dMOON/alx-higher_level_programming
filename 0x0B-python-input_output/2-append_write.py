#!/usr/bin/python3
"""module that holds file appending function"""

def append_write(filename="", text=""):
    """function that appends text to end of file"""

    with open(filename, 'a', encoding ='utf-8) as f:
        f.write(text)

    return len(text)
