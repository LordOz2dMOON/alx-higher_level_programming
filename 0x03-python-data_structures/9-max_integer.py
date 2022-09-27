#!/usr/bin/python3

 """
 find the maximum value of a list
 Args:
    my_list - list to search
 Return:
    None - if list is empty
    maximum of list
 """
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        highest_number = 0
        for number in my_list:
            if number > highest_number:
                highest_number = number
        return highest_number
