# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""
# import numpy as np

# Counting sort
# 값의 범위를 알 때 사용 가능! : Histogram
# O(N)


def counting_sort(_arr=[], _range=0):
    # Histogram 생성
    his = [0] * _range

    for i in range(len(_arr)):
        his[_arr[i]] += 1

    return his


if __name__ == '__main__':
    # arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    # arr = np.random.randint(0, 100, size=50)
    arr = [int(input()) for i in range(int(input()))]

    arr = counting_sort(_arr=arr, _range=10000 + 1)

    for i in range(len(arr)):
        for j in range(arr[i]):
            print(i)
