# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections


if __name__ == '__main__':
    queue = collections.deque()
    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        command = sys.stdin.readline().strip()

        if command[:2] == 'pu':
            num = command.split(' ')[1]
            queue.append(num)
        if command[:2] == 'po':
            if not queue:
                print(-1)
                continue
            print(queue.popleft())
        if command[0] == 's':
            print(len(queue))
        if command[0] == 'e':
            if queue:
                print(0)
                continue
            print(1)
        if command[0] == 'f':
            if not queue:
                print(-1)
                continue
            print(queue[0])
        if command[0] == 'b':
            if not queue:
                print(-1)
                continue
            print(queue[-1])



