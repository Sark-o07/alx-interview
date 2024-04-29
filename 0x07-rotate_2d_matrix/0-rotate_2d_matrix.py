#!/usr/bin/python3
"""Module that defines a function which
Rotates nxn 2D matrix 90° clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    function which rotates nxn 2D matrix 90° clockwise
    Args:
        matrix(list): 2D matrix
    Returns:
        None
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp
