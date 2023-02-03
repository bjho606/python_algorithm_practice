# 연결 요소의 개수

import sys

sys.setrecursionlimit(10**7)    # 최대 회귀 제한 늘리기

def dfs(i):
    visited[i] = 1
    for j in range(1, N+1):
        if graph[i][j] == 1 and visited[j] == 0:
            dfs(j)

N, M = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

count = 0

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)