# (다시) 아이디어가..
# 트리의 지름

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

def dfs(node):
    for next_node, weight in tree[node]:
        if visited[next_node] == -1:
            # temp_length += weight
            # dfs(next_node)
            # temp_length -= weight
            visited[next_node] = visited[node] + weight
            dfs(next_node)
    
for i in range(n-1):
    node1, node2, weight = map(int, input().split())
    tree[node1].append((node2, weight))
    tree[node2].append((node1, weight))
# print(tree)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1)

# print(visited)
largest_node = visited.index(max(visited))

visited = [-1] * (n+1)
visited[largest_node] = 0
dfs(largest_node)

print(max(visited))