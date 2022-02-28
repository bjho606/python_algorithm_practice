# 스티커

import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())

    upper = list(map(int, sys.stdin.readline().split()))
    lower = list(map(int, sys.stdin.readline().split()))

    dp = [[0,0,0] for _ in range(n)]
    dp[0][0] = upper[0]
    dp[0][1] = lower[0]
    dp[0][2] = 0            # no sticker
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + upper[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + lower[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))