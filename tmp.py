# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:50:29 2020

@author: SHIN

"""

from collections import deque


def compare(x):
    if x is "ICN":
        return False
    return True


def dfs(result=[], ticket=[], tickets=[], v=[]):
    if sum(v) == len(v):
        result.append(ticket[1])
        return True

    for idx, current in enumerate(tickets):
        # 사용한 티켓은 건너뛰기
        if v[idx]:
            continue

        # 이동 가능한 티켓 삽입
        if ticket[1] == current[0]:
            # 방문
            v[idx] = 1
            result.append(current[0])

            if dfs(result=result, ticket=current, tickets=tickets, v=v):
                return True

            v[idx] = 0
            del result[len(result) - 1]

    return False


def solution(tickets):
    answer = []

    # ICN 출발 기준 alphabet 순 정렬
    tickets.sort(key=lambda x: (compare(x[0]), x[1]))

    # 사용한 티켓
    v = [0] * len(tickets)

    # 시작
    ticket = tickets[0]
    v[0] = 1
    answer.append(ticket[0])

    dfs(result=answer, ticket=ticket, tickets=tickets, v=v)

    return answer


def main():
    # tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
    # tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
    tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
    # ["ICN", "COO", "ICN", "BOO", "DOO"]
    print(solution(tickets))


if __name__ == "__main__":
    main()
