# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""
import numpy as np

# Selection_Sort
# 가장 작은 것을 선택해서 제일 앞으로 보낸다!
# O(N ^ 2)

if __name__ == '__main__':
    #arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    arr = np.random.randint(0, 100, size=50)
    for i in range(len(arr) - 1):
        min_v = arr[i]
        idx = i
        for j in range(i + 1, len(arr)):
            if min_v > arr[j]:
                min_v = arr[j]
                idx = j

        arr[idx], arr[i] = arr[i], min_v

    print(arr)
