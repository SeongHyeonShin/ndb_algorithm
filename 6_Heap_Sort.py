# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""
import numpy as np

# Heap sort
# 이진 트리 기반 Heap을 이용하여 정렬
# O(N * log(N))


def heap_sort(_arr=[]):
    # 힙을 구성
    for i in range(1, len(_arr)):
        c = i
        while True:
            root = (c - 1) // 2
            if _arr[root] < _arr[c]:
                _arr[root], _arr[c] = _arr[c], _arr[root]
            c = root

            if c != 0:
                continue
            break

    # 크기를 줄여가며 반복적으로 힙을 구성
    for i in range(len(_arr) - 1, 0, -1):
        _arr[i], _arr[0] = _arr[0], _arr[i]

        root = 0
        while True:
            c = 2 * root + 1

            # 자식 중에 더 큰 값 찾기
            if c < i - 1 and _arr[c] < _arr[c + 1]:
                c += 1

            if c < i and _arr[root] < _arr[c]:
                _arr[root], _arr[c] = _arr[c], _arr[root]
            root = c

            if c < i:
                continue
            break


if __name__ == '__main__':
    # arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    arr = np.random.randint(0, 100, size=50)
    # arr = [int(input()) for i in range(int(input()))]

    heap_sort(_arr=arr)
    for i in range(len(arr)):
        print(arr[i])
