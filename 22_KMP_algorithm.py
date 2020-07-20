# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections

# Kruth-Morris-Pratt algorithm : 문자열 매칭 알고리즘
# 접두사와 접미사의 최대일치 길이를 계산
# e.g. : abcab : 최대일치길이 (2)


def makeTable(pattern=''):
    table = [0] * len(pattern)

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] is not pattern[j]:
            j = table[j - 1]

        if pattern[i] is pattern[j]:
            table[i] = j + 1
            j += 1

    return table


def KMP(parent='', pattern=''):
    # if pattern in parent:
    #     return True
    # return False
    table = makeTable(pattern=pattern)
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] is not pattern[j]:
            j = table[j - 1]

        if parent[i] is pattern[j]:
            if j is len(pattern) - 1:
                print(i - len(pattern) + 2)
                j = table[j]
            else:
                j += 1


def main():
    parent = 'ababacabacaabacaaba'
    pattern = 'abacaaba'
    KMP(parent=parent, pattern=pattern)


if __name__ == "__main__":
    main()
