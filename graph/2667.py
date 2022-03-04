# 단지 번호 붙이기

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y):
    q = deque()
    q.append((x, y))
    # print(q)
    visited[x][y] = 1
    count = 1

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 1 or next_x > N or next_y < 1 or next_y > N:
                continue
            if graph[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                q.append((next_x, next_y))
                count += 1
    
    return count

N = int(input())
    
graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    graph[i] = [-1] + list(map(int, input().rstrip('\n')))

ans = []
# print(graph)
for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 1 and visited[i][j] == 0:
                ans.append(dfs(i, j))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])