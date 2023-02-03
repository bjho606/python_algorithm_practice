# 좌표 정렬하기2

import sys

arr = []

N = int(sys.stdin.readline().strip())
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y,x])

arr.sort()

for i in range(N):
    print(arr[i][1], arr[i][0])