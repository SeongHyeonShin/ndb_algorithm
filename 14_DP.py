# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys

# DP : 하나의 문제를 단 한 번만 풀도록 하는 알고리즘
# 일반적인 분할 정복은 동일한 문제를 다시 푼다는 단점이 존재 (정렬 제외)
# 메모이제이션 (Memoization) 사용
# 재귀를 이용한 방법은 연산량이 2^n으로 폭발해버림


if __name__ == '__main__':
    # Baekjoon : 11726
    # 규칙을 통한 점화식이 필요함
    N = int(sys.stdin.readline().strip())

    if N > 1:
        memory = [0] * N
        memory[0], memory[1] = 1, 2

        # command = sys.stdin.readline().strip()
        # N, M = command.split(' ')[0], command.split(' ')[1]

        for i in range(2, N):
            memory[i] = memory[i - 1] + memory[i - 2]

        print(memory[N - 1] % 10007)
    else:
        print(1)
