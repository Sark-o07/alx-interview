#!/usr/bin/python3
"""
Solution to island_perimeter task.
"""


def island_perimeter(grid):
    """
    Calculates the island perimeter.
    Args:
        grid(list[list]): 2D array of integers.
    Returns:
        perimeter of the island.
    """

    rows = len(grid)
    col = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(col):
            if grid[i][j] == 1:
                # We start with the assumption that
                # the land is surrounded by water.
                perimeter += 4

                # Checks to see if there are vertical neighbor(s)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Checks to see if there are horizontal neightbor(s)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
