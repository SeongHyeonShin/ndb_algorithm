# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

def sum_number(arr=[]):
    total = 0
    for ii in arr:
        if ii.isdigit():
            total += int(ii)

    return total


if __name__ == '__main__':
    arr = [input() for i in range(int(input()))]

    arr.sort(key=lambda x:(len(x),sum_number(x), x))

    for i in range(len(arr)):
        # if i > 0 and arr[i] == arr[i - 1]:
        #     continue
        print(arr[i])

