#!/usr/bin/python3
"""Solution to minimum operations task.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result
    in exactly n 'H' characters in the file
    Args:
        n (int): number of characters needed to be written to the file
    """

    operations = 0
    minimum_op = 2

    while n > 1:
        while n % minimum_op == 0:
            operations += minimum_op
            n /= minimum_op
        minimum_op += 1
    return operations
