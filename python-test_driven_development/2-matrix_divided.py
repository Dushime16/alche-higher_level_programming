#!/usr/bin/python3
"""
Module for matrix_divided method.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int, float): The number to divide all elements by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list: A new matrix containing the divided elements.
    """
    type_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(type_err)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(type_err)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(type_err)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
