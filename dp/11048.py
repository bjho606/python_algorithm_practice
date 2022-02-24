# 이동하기

import sys

N, M = map(int, sys.stdin.readline().split())
miro = []
count = []
for i in range(N+1):
    miro.append([0] * (M+1))
    count.append([0] * (M+1))
# print(count)
for i in range(1, N+1):
    miro[i] = [0] + list(map(int, sys.stdin.readline().split()))
# print(miro)

count[1][1] = miro[1][1]
for i in range(1, N+1):
    for j in range(1, M+1):
        if i == j == 1: continue
        count[i][j] = max(count[i-1][j], count[i][j-1], count[i-1][j-1]) + miro[i][j]

print(count[N][M])