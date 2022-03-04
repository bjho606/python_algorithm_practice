# 텀 프로젝트

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(node):
    global student
    visited[node] = 1
    cycle.append(node)

    if visited[graph[node]] == 0:
        dfs(graph[node])
    elif visited[graph[node]] == 1 and graph[node] in cycle:
        # if graph[node] == node:
        #     student -= 1
        #     return
        start = cycle.index(graph[node])
        end = len(cycle)
        student -= end - start

T = int(input())

for i in range(T):
    N = int(input())
    graph = [[0] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    student = N

    graph = [0] + list(map(int, input().split()))
    # print(graph)
    for i in range(1, N+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)

    print(student)