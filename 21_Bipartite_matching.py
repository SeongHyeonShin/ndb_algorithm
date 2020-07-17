# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections

# 이분 매칭 : 네트워크 플로우 알고리즘과 연계
# 표현 방식 : 유량 / 용량
#

MAX = 101
INF = 1000000000
d = [0] * MAX
a = {}


# 매칭에서 성골한 경우 True, 실패한 경우 False
def dfs(c=[], x=0):
    # 연결된 모든 노드에 대해서 들어갈 수 있는 시도
    for i in range(len(a[x])):
        t = a[x][i]

        # 이미 처리한 노드
        if c[t]:
            continue
        c[t] = 1

        # 비어있거나 점유 노드에 더 들어갈 공간이 있는 경우
        if d[t] is 0 or dfs(c, d[t]):
            d[t] = x
            return True

    return False


def main():
    node = [[1, 2, 3],
            [1],
            [2]]

    for i in range(len(node)):
        if i + 1 not in a:
            a[i + 1] = []

        for data in node[i]:
            a[i + 1].append(data)

    count = 0
    n = 3
    for i in range(1, n + 1):
        c = [0] * MAX
        if dfs(c, i):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
