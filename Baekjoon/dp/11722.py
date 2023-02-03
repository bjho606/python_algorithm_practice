# 가장 긴 감소하는 부분 수열

import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            dp[i] = max(dp[i], 1)

print(max(dp))