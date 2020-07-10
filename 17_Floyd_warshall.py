# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys

# 플로이드 와샬 알고리즘 : 모든 정점에서 모든 정점으로의 최단 경로
# 다익스트라 알고리즘은 가장 적은 비용을 하나씩 선택 -> 플로이드 와샬은 거처가는 정점을 기준으로 수행


numofnode = 4
INF = 10000000000

dis = [[0, 5, INF, 8],
       [7, 0, 9, INF],
       [2, INF, 0, 4],
       [INF, INF, 3, 0]]


def floyd_whashall():
    # 결과 그래프 초기화
    cost = dis.copy()

    # k : 거쳐가는 노드
    for k in range(numofnode):
        # i : 출발 노드
        for i in range(numofnode):
            # j : 도착 노드
            for j in range(numofnode):
                if cost[i][k] + cost[k][j] < cost[i][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]

    print(cost)


if __name__ == "__main__":
    floyd_whashall()
    