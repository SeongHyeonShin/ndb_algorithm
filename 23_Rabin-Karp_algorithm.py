# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections

# Rabin-karp algorithm : 문자열 매칭 알고리즘
# 해시 기법 사용
# 긴 문자열을 짧은 데이터로 바꾸어주는 기법 : 해시값이 중복 될 겅유 (충돌) 포인터를 사용해 연결 자료구조로 해결


def RK(parent='', pattern=''):
    parentHash = 0
    patternHash = 0
    for i in range(len(pattern)):
        parentHash = parentHash * 2 + ord(parent[i])
        patternHash = patternHash * 2 + ord(pattern[i])

    power = 2 ** (len(pattern) - 1)
    for i in range(1, len(parent) - len(pattern) + 1):
        if parentHash == patternHash:
            print(i, '번째')

        parentHash = (parentHash - ord(parent[i - 1]) * power) * 2 + ord(parent[len(pattern) - 1 + i])

    if parentHash == patternHash:
        print(len(parent) - len(pattern) + 1, '번째')


def main():
    parent = 'ababacabacaabacaaba'
    pattern = 'abacaaba'
    RK(parent=parent, pattern=pattern)


if __name__ == "__main__":
    main()
