# DFS 와 BFS

from collections import deque
import sys

def dfs(v):
    print(v, end = ' ')
    dfs_visited[v] = 1
    for i in range(1, N+1):
        if dfs_visited[i] != 1 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    bfs_visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if bfs_visited[i] != 1 and graph[v][i] == 1:
                q.append(i)
                bfs_visited[i] = 1
    
N, M, V = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
# print(graph)
dfs_visited = [0 for _ in range(N+1)]
bfs_visited = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

dfs(V)
print()
bfs(V)