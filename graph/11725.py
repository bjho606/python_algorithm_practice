# 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(node):
    for i in graph[node]:
        if parents[i] == 0:
            parents[i] = node
            dfs(i)


N = int(input())

graph = [[] for _ in range(N+1)]
# print(graph)
for i in range(N-1):
    a, b = map(int, input().rstrip('\n').split())
    graph[a].append(b)
    graph[b].append(a)
parents = [0 for _ in range(N+1)]
# print(graph)
# print(parents)

dfs(1)

for i in range(2, N+1):
    print(parents[i])