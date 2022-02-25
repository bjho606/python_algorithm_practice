# 오르막 수

import sys

N = int(sys.stdin.readline())

# 2차원 배열 선언법 1
dp = []
for i in range(N+1):
    dp.append([0]*10)

# 2차원 배열 선언법 2 -> 이렇게 하면 값을 변경하려 할 때 배열의 모든 값이 다 바뀐다..! 아마 참조 문제랑 관련이 있는듯..
# dp = [[0] * 10] * (N+1)
# print(dp)
for i in range(10):
    dp[1][i] = 1
# print(dp)
    
for i in range(2, N+1):
    for j in range(0, 10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

count = 0
for i in range(10):
    count += dp[N][i]

print(count%10007)