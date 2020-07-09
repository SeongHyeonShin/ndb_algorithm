# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import math

# 에라토스테네스의 체 : 대표적인 소수 (prime number) 판별 알고리즘
# 소수를 대량으로 빠르고 정확하게 구하는 방법


def isPrimeNumber(x=0):
    # V1 : 무식하게 다해보기
    # for i in range(2, x):
    #     if x % i is 0:
    #         return False
    #     return True

    # V2 : sqrt(x)까지만 동작
    stop = int(math.sqrt(x))
    for i in range(2, stop):
        if x % i != 0:
            return False
        return True


def SieveofEratoshenes(M=0, N=0):
    if M == 1:
        M += 1

    _list = [0] * (N + 1)
    result = []
    # 1. 이자원 배열을 생성하여 값을 초기화
    for i in range(1, len(_list)):
        _list[i] = i

    # 2. 2부터 시작하여 특정 숫자의 배수에 해당하는 숫자를 모두 제거
    for i in range(2, len(_list)):
        if _list[i]:
            for j in range(i * 2, len(_list), i):
                if _list[j] % _list[i] == 0:
                    _list[j] = 0

    for i in range(M, len(_list)):
        if _list[i]:
            result.append(_list[i])

    return result


if __name__ == '__main__':
    command = sys.stdin.readline().strip()

    M, N = int(command.split(' ')[0]), int(command.split(' ')[1])

    for primenumber in SieveofEratoshenes(M=M, N=N):
        print(primenumber)