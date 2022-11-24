#!/usr/bin/python3
"""module that contains a function that uses json to write to a file"""
import json

def save_to_json_file(my_obj, filename):
    """function that writes to a text file using json"""
    with open(filename, 'w') as f:
       f.write( json.dumps(my_obj))


