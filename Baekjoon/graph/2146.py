# 다리 만들기 (다시 해보기 - 시간초과)

from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0,0,1,-1], [1,-1,0,0]
def dfs(x,y):
    global group
    q = deque()
    visited[x][y] = 1
    graph[x][y] = group
    q.append((x,y))

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if graph[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                q.append((next_x, next_y))
                graph[next_x][next_y] = group
                visited[next_x][next_y] = 1

def bfs(land):
    global ans
    q = deque()
    min_dist = [[-1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == land:
                q.append((i, j))
                min_dist[i][j] = 0

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if graph[next_x][next_y] != land and graph[next_x][next_y] != 0:
                ans = min(ans, min_dist[cur_x][cur_y])
                return
            if graph[next_x][next_y] == 0 and min_dist[next_x][next_y] == -1:
                min_dist[next_x][next_y] = min_dist[cur_x][cur_y] + 1
                q.append((next_x, next_y))

    # print(min_dist)

N = int(input())

graph = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().rstrip('\n').split()))
visited = [[0 for _ in range(N)] for _ in range(N)]
# print(graph)

group = 1

# 섬 구분하기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            group += 1
# print(visited)
# print(graph)

# 답 찾기
ans = (N-1) * 2
for i in range(1, group):
    bfs(i)

print(ans)