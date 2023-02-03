# 이분 그래프

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            if dfs(i, -group) == False:
                return False
        elif visited[i] == visited[v]:
            return False

    return True

K = int(sys.stdin.readline())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    ans = True

    for i in range(1, V+1):
        if visited[i] == 0:
            ans = dfs(i, 1)
        if ans == False:
            break

    if ans:
        print('YES')
    else:
        print('NO')