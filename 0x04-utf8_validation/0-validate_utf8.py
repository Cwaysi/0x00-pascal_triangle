#!/usr/bin/python3
"""
Define a valid UTF-8 encoding.
"""
from itertools import takewhile


def bits(numbers):
    """
    function
    """
    for num in numbers:
        byt = []
        seen = 1 << 8  
        while seen:
            seen >>= 1
            byt.append(bool(num & seen))
        yield byt


def validUTF8(data):
    """
    True or False
    """
    ubits = bits(data)
    for byte in ubits:
        if byte[0] == 0:
            continue
        one_s = sum(takewhile(bool, byte))
        if one_s <= 1:
            return False
        if one_s >= 4:  
            return False
        for _ in range(one_s - 1):
            try:
                byte = next(ubits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
