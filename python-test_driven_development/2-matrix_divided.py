#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
            matrix (list): A matrix (list of lists) of integers/floats.
            div (int or float): The number to divide the matrix elements by.

    Returns:
            list: A new matrix with the elements divided by the given number.

    Raises:
            TypeError: If the matrix is not a matrix (list of lists) of integers/floats,
                               or if the matrix rows have different sizes.
            TypeError: If the div is not a number.
            ZeroDivisionError: If the div is zero.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for num in [num for row in matrix for num in row]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
