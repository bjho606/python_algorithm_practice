# 2xN 타일링 2

import sys

n = int(sys.stdin.readline())

dp = [0, 1, 3]

for i in range(3, n+1):
    count = 0
    count += dp[i-1] + dp[i-2] * 2
    dp.append(count)

print(dp[n]%10007)