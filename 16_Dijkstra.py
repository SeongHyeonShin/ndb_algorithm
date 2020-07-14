# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys
import heapq
from collections import defaultdict
# 다익스트라 알고리즘 : 최단 경로 탐색 알고리즘
# DP or Greedy search 기반 알고리즘
# 하나의 노드로 부터 다른 모든 노드로 가는 최단 경로를 계산

INF = 1000000000

num = 6
visit = [0] * num
cost = [0] * (num + 1)
dis = {i: i for i in range(num + 1)}

# 선형 탐색 : O(N^2) 비효율
"""
def getSmallIndex():
    min_v = INF
    idx = 0
    for j in range(len(cost)):
        if min_v > cost[j] and not visit[j]:
            min_v = cost[j]
            idx = j

    return idx


def dijkstra(start=0, dis=[]):
    for i in range(len(dis[start])):
        cost[i] = dis[start][i]
    visit[start] = 1

    for i in range(num - 2):
        c_idx = getSmallIndex()
        visit[c_idx] = 1

        for j in range(num):
            if not visit[j]:
                cost[j] = min(cost[j], cost[c_idx] + dis[c_idx][j])


if __name__ == '__main__':
    # command = sys.stdin.readline().strip()
    # M, N = int(command.split(' ')[0]), int(command.split(' ')[1])

    dis = [[0, 2, 5, 1, INF, INF],
           [2, 0, 3, 2, INF, INF],
           [5, 3, 0, 3, 1, 5],
           [1, 2, 3, 0, 1, INF],
           [INF, INF, 1, 1, 0, 2],
           [INF, INF, 5, INF, 2, 0]]

    dijkstra(0, dis=dis)
    print(cost)
"""


class PriorityQueue():
    def __init__(self):
        self.queue = []

    def enqueue(self, v, priority):
        heapq.heappush(self.queue, (priority, v))

    def top(self):
        return self.queue[0]

    def pop(self):
        return heapq.heappop(self.queue)

    def display(self):
        print(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def size(self):
        return len(self.queue)


def dijkstra(start=0):
    cost[start] = 0
    pq = PriorityQueue()    # heap 구조
    pq.enqueue(start, 0)

    # 가까운 순서대로 처리
    while not pq.empty():
        c_idx = pq.top()[1]
        #
        distance = pq.top()[0]
        pq.pop()

        # 최단거리가 아니면 skip
        if cost[c_idx] < distance:
            continue

        for i in range(len(dis[c_idx])):
            # 선택된 노드의 인접 노드
            next = dis[c_idx][i][0]
            # 선택된 노드를 거쳐서 인접 노드로 가는 비용
            nextDistance = distance + dis[c_idx][i][1]

            if nextDistance < cost[next]:
                cost[next] = nextDistance
                pq.enqueue(next, nextDistance)


if __name__ == "__main__":
    numbers =[30, 3]
    solution(numbers=numbers)

    for i in range(1, num + 1):
        cost[i] = INF

    dis[1].append([2, 2])
    dis[1].append([3, 5])
    dis[1].append([4, 1])

    dis[2].append([1, 2])
    dis[2].append([3, 3])
    dis[2].append([4, 2])

    dis[3].append([1, 5])
    dis[3].append([2, 3])
    dis[3].append([4, 3])
    dis[3].append([5, 1])
    dis[3].append([6, 5])

    dis[4].append([1, 1])
    dis[4].append([2, 2])
    dis[4].append([3, 3])
    dis[4].append([5, 1])

    dis[5].append([3, 1])
    dis[5].append([4, 1])
    dis[5].append([6, 2])

    dis[6].append([3, 5])
    dis[6].append([5, 2])
    dijkstra(1)

    print(cost[1:])