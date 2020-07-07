# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""
import numpy as np

# Bubble sort
# 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보낸다
# O(N ^ 2)

if __name__ == '__main__':
    # arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    arr = np.random.randint(0, 100, size=50)

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)
