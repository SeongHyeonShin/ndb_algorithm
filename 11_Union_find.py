# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections


def getParent(parent=[], x=0):
    if parent[x] == x:
        return x

    return getParent(parent, parent[x])


def unionParent(parent=[], a=0, b=0):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def findParent(parent=[], a=0, b=0):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a == b:
        return 1
    else:
        return 0


if __name__ == '__main__':
    """
    parent = [0] * 11
    for i in range(1, len(parent)):
        parent[i] = i

    unionParent(parent, 1, 2)
    unionParent(parent, 2, 3)
    unionParent(parent, 3, 4)
    unionParent(parent, 5, 6)
    unionParent(parent, 7, 8)
    print(findParent(parent, 1, 5))

    unionParent(parent, 1, 5)
    print(findParent(parent, 1, 5))
    """

    # BJ : 2606
    numofcomputer = int(sys.stdin.readline().strip())
    numofedge = int(sys.stdin.readline().strip())

    parent = [0] * (numofcomputer + 1)
    for i in range(1, len(parent)):
        parent[i] = i

    for i in range(numofedge):
        command = sys.stdin.readline().strip()
        a, b = int(command.split(' ')[0]), int(command.split(' ')[1])

        unionParent(parent, a, b)

    count = 0
    for i in range(2, numofcomputer + 1):
        if getParent(parent, 1) == getParent(parent, i):
            count += 1

    print(count)

