# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""
import numpy as np

# Insertion sort
# 각 숫자를 적절한 위치에 삽입한다!
# O(N ^ 2)

if __name__ == '__main__':
    # arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    arr = np.random.randint(0, 100, size=50)
    for i in range(len(arr) - 1):
        j = i
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    print(arr)
