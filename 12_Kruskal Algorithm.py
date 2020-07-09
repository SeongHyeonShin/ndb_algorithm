# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys

# 크루스칼 알고리즘 : 가장 적은 비용으로 모든 노드를 연결
# 간선 숫자는 반드시 node 개수 - 1:
# e.g. node가 7일때 간선은 6


def getParent(parent=[], x=0):
    if parent[x] is x:
        return x

    return getParent(parent, parent[x])


def unionParent(parent=[], a=0, b=0):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def findParent(parent=[], a=0, b=0):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a is b:
        return 1
    else:
        return 0


class Edge():
    def __init__(self, a=0, b=0, dis=0):
        self.a = a
        self.b = b
        self.distance = dis


if __name__ == '__main__':
    # Baekjoon : 1197
    command = sys.stdin.readline().strip()
    V, E = int(command.split(' ')[0]), int(command.split(' ')[1])

    cost = 0

    # cycle
    node = [0] * (V + 1)
    for i in range(1, len(node)):
        node[i] = i

    edge_list = []

    for _ in range(E):
        command = sys.stdin.readline().strip()
        a, b, dis = int(command.split(' ')[0]), int(command.split(' ')[1]), int(command.split(' ')[2])
        edge_list.append(Edge(a=a, b=b, dis=dis))

    edge_list.sort(key=lambda x: x.distance)
    count = 0

    for i in range(len(edge_list)):
        if not findParent(node, edge_list[i].a, edge_list[i].b):
            unionParent(node, edge_list[i].a, edge_list[i].b)
            cost += edge_list[i].distance
            count += 1

        if count is V - 1:
            break

    print(cost)




