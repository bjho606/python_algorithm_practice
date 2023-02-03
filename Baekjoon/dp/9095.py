# 1, 2, 3 더하기

import sys

n = int(sys.stdin.readline())
T = [0]
dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(1, n+1):
    T.append(int(sys.stdin.readline()))

# for i in range(n):
    for j in range(4, T[i]+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

    print(dp[T[i]])