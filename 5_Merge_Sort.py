# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""
# import numpy as np

# Merge sort
# 반으로 나누고 나중에 합쳐서 정렬 : 분할 정복
# O(N * log(N))


def merge(left=[], right=[]):
    left_idx = 0
    right_idx = 0

    result = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        for i in range(left_idx, len(left)):
            result.append(left[i])
    if right_idx < len(right):
        for i in range(right_idx, len(right)):
            result.append(right[i])

    return result


def merge_sort(_arr=[]):
    if len(_arr) <= 1:
        return _arr

    middle = len(_arr) // 2
    left = _arr[:middle]
    right = _arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


if __name__ == '__main__':
    # arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    # arr = np.random.randint(0, 100, size=50)
    arr = [int(input()) for i in range(int(input()))]

    arr = merge_sort(_arr=arr)
    for i in range(len(arr)):
        print(arr[i])
