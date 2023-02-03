# 병사 배치하기

import sys

input = sys.stdin.readline

N = int(input())
soldier = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if soldier[i] < soldier[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)

print(N - max(dp))