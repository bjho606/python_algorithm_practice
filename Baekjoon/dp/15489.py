# 파스칼 삼각형

import sys

input = sys.stdin.readline

R, C, W = map(int, input().split())

pascal_dp = [[1]*i for i in range(31)]

for i in range(2, 31):
    for j in range(1, i-1):
        pascal_dp[i][j] = pascal_dp[i-1][j-1] + pascal_dp[i-1][j]

# 확인
# for i in range(10):
#     for j in range(i):
#         print(pascal_dp[i][j], end=' ')
#     print()

sum = 0
for i in range(R, R+W):
    for j in range(C-1, C+(i-R)):
        # print(i, j)
        sum += pascal_dp[i][j]

print(sum)