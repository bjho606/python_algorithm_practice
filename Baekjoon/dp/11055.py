# 가장 큰 증가 부분 수열

import sys

a = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(a)]

dp[0] = arr[0]
for i in range(1, a): 
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])
        else:
            dp[i] = max(dp[i], arr[i])

print(max(dp))