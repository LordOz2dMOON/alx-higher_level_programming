#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """matrix_divided(matrix, div) function takes the div number and uses it to divide all numbers in the matrix"""
    for i in range (len(matrix)):
        for j in range(len(matrix):
            if not all(isinstance(item, int or float) for item in matrix):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not type(div) is int or float:
        raise TyperError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])


