# 가장 긴 바이토닉 부분 수열

import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]
reverse_dp = [0 for _ in range(N)]

dp[0] = 1
reverse_dp[N-1] = 1

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            dp[i] = max(dp[i], 1)

        # if arr[i] < arr[j]:
        #     reverse_dp[i] = max(reverse_dp[i], reverse_dp[j] + 1)
        # else:
        #     reverse_dp[i] = max(reverse_dp[i], 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            reverse_dp[i] = max(reverse_dp[i], reverse_dp[j] + 1)
        else:
            reverse_dp[i] = max(reverse_dp[i], 1)

# print(dp)
# print(reverse_dp)

sum = dp[0] + reverse_dp[0] - 1
for i in range(1, N):
    sum = max(dp[i] + reverse_dp[i] - 1, sum)

print(sum)