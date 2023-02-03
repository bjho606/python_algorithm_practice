# 미로 탐색

from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs():
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_x >= N or  next_y < 0 or next_y >= M:
                continue
            if graph[next_x][next_y] == 1:
                q.append((next_x, next_y))
                graph[next_x][next_y] = graph[cur_x][cur_y] + 1

N, M = map(int, input().split())

graph = [[-1 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().rstrip('\n')))

# print(graph)

q = deque()
q.append((0,0))

bfs()

print(graph[N-1][M-1])