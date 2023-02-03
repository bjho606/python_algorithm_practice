# 순열 사이클

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, group):
    global count

    visited[node] = group
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i, group)
        elif visited[i] == visited[node]:
            # print('visited', group)
            count += 1

T = int(input())

for i in range(T):
    N = int(input())

    graph = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    # print(graph)
    input_list = [0] + list(map(int, input().split()))
    for i in range(1, N+1):
        graph[i].append(input_list[i])

    # print(graph)
    count = 0

    # print(graph)
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i, i)

    print(count)