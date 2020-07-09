# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections

# Stack : FILO
# DFS (깊이 우선 탐색)에 사용


if __name__ == '__main__':
    stack = collections.deque()
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        command = sys.stdin.readline().strip()
        if command[:2] == "pu":
            num = int(command.split(' ')[1])
            stack.append(num)
        if command[:2] == "po":
            if not stack:
                print(-1)
                continue
            print(stack.pop())
        if command[0] == "s":
            print(len(stack))
        if command[0] == 'e':
            if stack:
                print(0)
                continue
            print(1)
        if command[0] == 't':
            if not stack:
                print(-1)
                continue
            print(stack[-1])


