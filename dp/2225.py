# 합분해 (다시)

# n = 1 ->  1
# n = 2 -> k=1:1 k=2:3 k=3:3+6+1

import sys

N, K = map(int, sys.stdin.readline().split())

dp = [1] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        print(i, j)
        dp[i] = dp[j] + dp[i-j]
        # for k in range(K):

print(dp[N])