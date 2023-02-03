# 파도반 수열

import sys

T = int(sys.stdin.readline())

P = [1,1,1,2,2,3,4,5,7,9]

N = []

for i in range(T):
    N = int(sys.stdin.readline())
    if N <= 10:
        print(P[N-1])
        continue

    dp = [1,1,1,2,2,3,4,5,7,9]
    for i in range(10, N):
        dp.append(dp[i-1] + dp[i-5])

    print(dp[N-1])