# 이친수

import sys

N = int(sys.stdin.readline())

pn = []
count = []
for i in range(N+1):
    pn.append([0, 1])
    count.append([0] * 2)
# print(pn)
count[1][1] = 1
# print(count)

for i in range(2, N+1):
    count[i][0] = count[i-1][1] + count[i-1][0]
    count[i][1] = count[i-1][0]

print(count[N][0] + count[N][1])