#!/usr/bin/python3
"""
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
check if a box is openable
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for w in range(1, len(boxes) - 1):
        visited_box = False
        for na in range(len(boxes)):
            visited_box = w in boxes[na] and w != na
            if visited_box:
                break
        if visited_box is False:
            return visited_box
    return True
