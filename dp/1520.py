# 내리막길 (다시하기)

import sys

def dfs(x, y):
    if x == M and  y == N:
        return 1
    
    
    return count[x][y]

N, M = map(int, sys.stdin.readline().split())
board = []
count = []
for i in range(N+1):
    board.append([0]*(M+1))
    count.append([0]*(M+1))
count[1][1] = 1

for i in range(1, N+1):
    board[i] = [0] + list(map(int, sys.stdin.readline().split()))

# print(board)
# print(count)
for i in range(1, N+1):
    for j in range(1, M+1):
        right = j + 1
        left = j - 1
        up = i - 1
        down = i + 1
        if left >= 1:
            if board[i][j] > board[i][left]:
                count[i][left] += count[i][j]
        if up >= 1:
            if board[i][j] > board[up][j]:
                count[up][j] += count[i][j]
        if right <= M:
            if board[i][j] > board[i][right]:
                count[i][right] += count[i][j]
        if down <= N:
            if board[i][j] > board[down][j]:
                count[down][j] += count[i][j]

print(count[N][M])