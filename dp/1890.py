# 점프

import sys

N = int(sys.stdin.readline())

board = []
count = []
for i in range(N+1):
    board.append([0] * (N+1))
    count.append([0] * (N+1))
count[1][1] = 1

for i in range(1, N+1):
    board[i] = [0] + list(map(int, sys.stdin.readline().split()))
# print(board)
# print(count)

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j == N: continue
        right = j+board[i][j]
        down = i+board[i][j]
        if right <= N:
            count[i][right] += count[i][j]
        if down <= N:
            count[down][j] += count[i][j]

print(count[N][N])