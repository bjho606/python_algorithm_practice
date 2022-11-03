# 상근이의 여행

import sys

input = sys.stdin.readline

def dfs(node):
    global count
    visited[node] = 1
    for country in countries[node]:
        if not visited[country]:
            count += 1
            dfs(country)

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    countries = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    count = 0
    for m in range(M):
        a, b = map(int, input().split())
        countries[a].append(b)
        countries[b].append(a)

    dfs(1)

    print(count)