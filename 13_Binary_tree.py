# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

import sys

# 이진 트리 : 데이터 탐색 속도 증진을 위해 사용하는 구조
# Preorder Traversal
# (1) 먼저 자기 자신을 처리
# (2) 왼쪽 자식을 방문
# (3) 오른쪽 자식을 방문

# Inorder Traversal
# (1) 왼쪽 자식을 방문합니다.
# (2) 자기 자신을 처리합니다.
# (3) 오른쪽 자식을 방문합니다.

# Postorder Traversal
# (1) 왼쪽 자식을 방문
# (2) 오른쪽 자식을 방문
# (3) 자기 자신을 처리


def preorder(node=[], data='', _list=[]):
    if node and data != '.':
        _list.append(data)
        preorder(node=node, data=node[data][0], _list=_list)
        preorder(node=node, data=node[data][1], _list=_list)


def inorder(node=[], data='', _list=[]):
    if node and data != '.':
        inorder(node=node, data=node[data][0], _list=_list)
        _list.append(data)
        inorder(node=node, data=node[data][1], _list=_list)


def postorder(node=[], data='', _list=[]):
    if node and data != '.':
        postorder(node=node, data=node[data][0], _list=_list)
        postorder(node=node, data=node[data][1], _list=_list)
        _list.append(data)


if __name__ == '__main__':
    # Baekjoon : 1991
    node_graph = {i: [] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        command = sys.stdin.readline().strip()
        data, left, right = command.split(' ')[0], command.split(' ')[1], command.split(' ')[2]
        node_graph[data] += [left, right]

    output = []
    preorder(node_graph, 'A', output)
    print("".join(output))

    output = []
    inorder(node_graph, 'A', output)
    print("".join(output))

    output = []
    postorder(node_graph, 'A', output)
    print("".join(output))
