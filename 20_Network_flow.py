# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections

# 네트워크 플로우 : 특정한 지점에서 다른 지점으로 데이터가 얼마나 많이 흐르고 있는가를 측정
# 표현 방식 : 유량 / 용량
# BFS 사용 : 에드몬드 카프 알고리즘
# 음의 유량을 계산
#

MAX = 101
INF = 1000000000
numofnode = 6
c = [[0] * MAX for _ in range(MAX)]
f = [[0] * MAX for _ in range(MAX)]
a = {}


def maxFlow(start=0, end=0):
    result = 0
    while True:
        d = [-1] * MAX
        q = collections.deque()
        q.append(start)

        while len(q):
            x = q.popleft()
            for i in range(len(a[x])):
                y = a[x][i]

                # 방문하지 않은 노드 중에서 용량이 남은 경우
                if c[x][y] - f[x][y] > 0 and d[y] == -1:
                    q.append(y)
                    d[y] = x

                    if y is end:
                        break

        # 모든 경로를 다 찾은 뒤에 탈출
        if d[end] == -1:
            break
        flow = INF

        i = end
        for _ in range(len(d)):
            if i == start:
                break

            flow = min(flow, c[d[i]][i] - f[d[i]][i])
            i = d[i]

        i = end
        for _ in range(len(d)):
            if i == start:
                break

            f[d[i]][i] += flow
            f[i][d[i]] -= flow
            i = d[i]

        result += flow

    print(result)


def main():
    node = [[1, 2, 12],
            [1, 4, 11],
            [2, 3, 6],
            [2, 4, 3],
            [2, 5, 5],
            [2, 6, 9],
            [3, 6, 8],
            [4, 5, 9],
            [5, 3, 3],
            [5, 6, 4]]

    for f, s, cost in node:
        if f not in a:
            a[f] = []
        a[f].append(s)

        if s not in a:
            a[s] = []
        a[s].append(f)

        c[f][s] = cost

    maxFlow(1, 6)


if __name__ == "__main__":
    main()
