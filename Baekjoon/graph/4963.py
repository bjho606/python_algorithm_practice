# 섬의 개수

from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def dfs(x, y):
    q = deque()
    visited[x][y] = 1
    q.append((x,y))
    count = 1

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(8):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            # print(next_x, next_y)
            if next_x < 1 or next_x > h or next_y < 1 or next_y > w:
                continue
            if graph[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                q.append((next_x, next_y))

    return count

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [[-1 for _ in range(w+1)] for _ in range(h+1)]
    for i in range(1, h+1):
        graph[i] = [-1] + list(map(int, input().rstrip('\n').split()))
    # print(graph)
    visited = [[0 for _ in range(w+1)] for _ in range(h+1)]

    count = 0

    for i in range(1, h+1):
        for j in range(1, w+1):
            if graph[i][j] == 1 and visited[i][j] == 0:
                count += dfs(i,j)

    print(count)