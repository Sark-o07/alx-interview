#!/usr/bin/python3

"""
the rules follows
if we have even set of prime numbers in given number ben wins
if odd maria wins
if there is no prime number at the start ben wins.
maria always goes first.
"""


def prime_count(n):
    """
    Determines the counts of prime number between 1 and
    the given number inclusive.
    Args:
        n (int): the given number
    Return:
        the count of prime numbers
    """

    # A True array ranging from 0 - n (n inclusive)
    prime_count = 0
    prime = [True for i in range(n + 1)]
    if n < 2:
        return prime_count

    # Starting with the first knoww prime num 2
    p = 2

    while (p * p <= n + 1):
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for i in range(2, n + 1):
        if prime[i]:
            prime_count += 1
    return prime_count


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    ben_score = 0
    maria_score = 0
    for i in range(x):
        primeCount = prime_count(nums[i])

        if primeCount == 0:
            ben_score += 1
        elif primeCount % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if ben_score > maria_score:
        return 'Ben'
    if maria_score > ben_score:
        return 'Maria'
    return None
