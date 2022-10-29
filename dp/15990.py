# 1,2,3 더하기 5

import sys

dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1][1] = 1
dp[3][1] = 1
dp[2][2] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3])%1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%1000000009   

# 확인
# for i in range(1, 4):
#     for j in range(10):
#         print(dp[j][i], end=' ')
#     print()

T = int(input())
for _ in range(T):
    num = int(input())
    sum = (dp[num][1] + dp[num][2] + dp[num][3])%1000000009

    print(sum)