#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        if letter == 'c' or letter == 'C':
             mydict = {99:  '', 67: ''}
             return my_string.translate(mydict)
