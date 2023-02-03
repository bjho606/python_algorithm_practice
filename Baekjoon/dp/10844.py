# 쉬운 계단 수

import sys

N = int(sys.stdin.readline())

dp = []
for i in range(N+1):
    dp.append([0]*10)

dp[1][0] = 0
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]

count = 0
for i in range(10):
    count += dp[N][i]

print(count%1000000000)