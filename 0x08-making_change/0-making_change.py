#!/usr/bin/python3
"""Coin change task solution.
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed
    to meet a given amount total
    Arg:
        coins(list): list of coin(s)
        total(int): total amount required
    Returns:
        count(int): number of coin(s) needed to meet the total
    """
    if (total <= 0):
        return 0
    coins.sort(reverse=True)
    sum = 0
    for coin in coins:
        if (total < coin):
            pass
        q, r = divmod(total, coin)
        sum += q
        total = r
        if (total == 0):
            return sum
    if (total != 0):
        return -1
