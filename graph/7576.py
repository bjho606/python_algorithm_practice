# 토마토

from collections import deque
import sys

dx, dy = [0,0,1,-1], [1,-1,0,0]

def bfs():
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if tomato[next_x][next_y] == 0:
                q.append((next_x, next_y))
                tomato[next_x][next_y] = tomato[cur_x][cur_y] + 1


input = sys.stdin.readline

M, N = map(int, input().split())

q = deque()
tomato = [[2 for _ in range(M)] for _ in range(N)]
for i in range(N):
    tomato[i] = list(map(int, input().rstrip('\n').split()))
count = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i,j))

# print(tomato)
bfs()
# print(tomato)

# 출력
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    count = max(count, max(i)-1)

print(count)