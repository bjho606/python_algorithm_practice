# 합분해 (다시)
# dp

# n = 1 -> 0,1 / 1,0
# n = 2 -> 0,2 / 2,0 / 1,1
# n = 3 -> 0,3 / 3,0 / 2,1 / 1,2
# n = 4 -> 0,4 / 4,0 / 3,1 / 1,3 / 2,2

# n = 1 -> 0,0,1 / 0,1,0 / 1,0,0
# n = 2 -> 0,0,2 / 0,2,0 / 2,0,0 / 0,1,1 / 1,1,0 / 1,0,1
# n = 3 -> 0,0,3 / 0,3,0 / 3,0,0 / 0,1,2 / 1,2,0 / 2,0,1 / 0,2,1 / 2,1,0 / 1,0,2 / 1,1,1

import sys

N, K = map(int, sys.stdin.readline().split())

dp = [0] * (N+1)
dp[1] = K

for i in range(1, N+1):
    for j in range(i):
        print(i, j)
        dp[i] = dp[j] + dp[i-j]
        # for k in range(K):

print(dp[N])