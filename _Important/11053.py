# 가장 긴 증가하는 부분 수열 -- LIS (Longest Increasing Subsequence)

import sys

A = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
dp = [1] * A

for i in range(A):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))