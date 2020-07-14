# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections

# 강한 결합 요소 : 그래프 안에서 '강하게 결합된 정점 집합'
# SCC는 '같은 SCC에 속한 두 정점은 서로 도달이 가능하다는 특징' : e.g. 사이클 발생
# 무향 그래프는 다 SCC : 큰 의미 없음
# 코사라주 알고리즘과 타잔 알고리즘 존재 : 타잔 알고리즘이 적용이 쉬움
# DFS 사용

MAX = 10001
id_v = [0]
d = [0] * MAX
finished = [0] * MAX
s = collections.deque()
edge = {}
SCC = []


# DFS는 총 정 점의 갯수만큼 실행
def dfs(x=0):
    id_v[0] += 1
    d[x] = id_v[0]   # 노드마다 고유 번호 할당
    s.append(x) # 스택에 자기 자신 삽입

    parent = d[x]
    for i in range(len(edge[x])):
        y = edge[x][i]

        if d[y] == 0: # 방문하지 않은 이웃
            parent = min(parent, dfs(y))
        elif not finished[y]: # 처리 중인 이웃
            parent = min(parent, d[y])

    if parent is d[x]:
        scc = collections.deque()
        while True:
            t = s.pop()
            scc.append(t)

            finished[t] = 1
            if t is x:
                break
        SCC.append(scc)

    return parent


def main():
    v = 11
    node = [[2],
            [3],
            [1],
            [2, 5],
            [7],
            [5],
            [6],
            [5, 9],
            [10],
            [11],
            [3, 8]]

    for i in range(v):
        if i + 1 not in edge:
            edge[i + 1] = []

        for e in node[i]:
            edge[i + 1].append(e)

    for i in range(1, v + 1):
        if d[i] is 0:
            dfs(i)

    print("SCC 갯수 : %d" % len(SCC))
    for i in range(len(SCC)):
        print("%d번째 SCC : " % (i + 1))
        print(SCC[i])


if __name__ == "__main__":
    main()
    