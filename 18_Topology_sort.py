# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import collections

# 위상 정렬 : 순서가 정해져 있는 작업을 차례로 수행해야 할 때 그 순서를 결정
# DAG(Directed Acycle Graph)에만 적용가능
# 현재 그래프는 위상 정렬이 가능한지
# 위상정렬이 가능하다면 그 결과를 리턴 : stack or queue를 사용 (queue를 더 많이 사용)


# 1. 진입차수가 0인 정점을 큐에 삽입 (진입 차수란 현재 노드로 들어오는 노드 수 : 현재 노드를 수행하기 위한 선행조건)
# 2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거
# 3. 간선 제거 이후 진입차수가 -이 된 정점을 큐에 삽입
# 4. 큐가 빌 때까지 2 ~ 3번 과정 반복 : 모든 원소를 방문하기 전에 큐가 빈다면 사이클 존재!


numofnode = 7
inDegree = [0] * (numofnode + 1)
edge = {}


def topologySort():
    result = []
    q = collections.deque()

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, len(inDegree)):
        if inDegree[i] == 0:
            q.append(i)

    # 모든 노드에 대해 방문
    for i in range(1, len(inDegree)):
        # n 개를 방문하기 전에 끝나면 사이클 발생
        if len(q) == 0:
            print("사이클 발생")
            return

        data = q.popleft()
        result.append(data)

        for j in range(len(edge[data])):
            tmp = edge[data][j]
            inDegree[tmp] -= 1
            if inDegree[tmp] == 0:
                q.append(tmp)

    print(result)


def main():
    node = [1, 2, 3, 4, 5, 6, 7]
    direction = [[0],
                 [2, 5],
                 [3],
                 [4],
                 [6],
                 [6],
                 [7],
                 []]

    for tmp in node:
        if tmp in edge:
            for data in direction[tmp]:
                edge[tmp].append(data)
                inDegree[data] += 1
        else:
            edge[tmp] = []
            if len(direction[tmp]):
                for data in direction[tmp]:
                    edge[tmp].append(data)
                    inDegree[data] += 1

    topologySort()


if __name__ == "__main__":
    main()
    