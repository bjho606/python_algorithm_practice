# 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().split())

lans = []
for i in range(K):
    lans.append(int(sys.stdin.readline().strip()))

start, end = 1, max(lans)

while start <= end:
    mid = (end+start)//2
    count = 0
    for lan in lans:
        count += lan // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
