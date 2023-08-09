#!/usr/bin/python3
"""
In a text file, there is a single character H.
"""


def minOperations(n: int) -> int:
    """Calculate the fewest no. of operations """
    ter = 0
    mori = 2
    while n > 1:
        while not n % mori:
            ter += mori
            n /= mori
        mori += 1
    return ter
