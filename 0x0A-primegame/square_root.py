#!/usr/bin/python3

# we need n the number to find its root.
# e (tolerance level)
# g (guess) root we are going to start with.
# applying newton's method.

def square_root(n):
    """
    Finds the square root of a given number n
    Args:
        (n): the given number.
    Returns:
        the square root of the number n.
    """
    
    guess = n / 2
    e = 0.00001
    
    while abs( guess * guess - n) > e :
        # update guess with average guess and n divided by guess
        guess = (guess + n / guess) / 2
    
    return guess

root = square_root(49)
print(root)