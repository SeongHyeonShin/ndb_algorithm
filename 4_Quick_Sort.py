# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""
import numpy as np

# Quick sort
# 특정 값을 기준으로 큰 숫자와 작은 숫자를 나눈다 : 분할 정복
# Max : O(N ^ 2), Min : O(N * log(N))


def quick_sort(_arr=[], start=0, end=0):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end - 1

    while left <= right:
        while left <= end - 1 and _arr[left] <= _arr[pivot]:
            left += 1
        while right > start and _arr[right] >= _arr[pivot]:
            right -= 1

        if left <= right:
            _arr[left], _arr[right] = _arr[right], _arr[left]
        else:
            _arr[pivot], _arr[right] = _arr[right], _arr[pivot]

    quick_sort(_arr=_arr, start=start, end=right)
    quick_sort(_arr=_arr, start=right + 1, end=end)


if __name__ == '__main__':
    # arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    arr = np.random.randint(0, 100, size=50)

    quick_sort(_arr=arr, start=0, end=len(arr))

    print(arr)
