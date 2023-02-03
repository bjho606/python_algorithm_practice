# 구간 합 구하기 5

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [[0]*(N+1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]
# print(board)
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = board[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(M):
    sums = 0
    x1, y1, x2, y2 = map(int, input().split())
    # 시간초과
    # for row in range(x1, x2+1):
    #     for col in range(y1, y2+1):
    #         # print(row, col)
    #         sums += board[row][col]

    sums = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1])

    print(sums)
