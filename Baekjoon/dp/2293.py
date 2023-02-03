# 동전1

import sys

n, k = map(int, sys.stdin.readline().split())

dp = [0] * (k+1)
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
dp[0] = 1

for i in coin:
    for j in range(1, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])