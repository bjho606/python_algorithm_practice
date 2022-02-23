# 공유기 설치

import sys

N, C = map(int, sys.stdin.readline().split())
houses = []
for i in range(N):
    houses.append(int(sys.stdin.readline().strip()))

houses.sort()
start, end = 1, houses[-1] - houses[0]   # 거리의 차의 최소, 최대
ans = 1

while start <= end:
    mid = (start + end) // 2
    count = 1
    temp = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - temp >= mid:
            count += 1
            temp = houses[i]

    if count >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)