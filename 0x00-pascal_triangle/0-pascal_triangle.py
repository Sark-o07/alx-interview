#!/usr/bin/python3

def pascal_triangle(n):
    """
    The function takes in an int n and generates a pascals triangle of n rows.
    Args:
        n (int): number of rows for the triangle.
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif 0 < j < i:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
