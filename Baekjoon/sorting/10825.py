# 국영수

import sys

arr = []

N = int(sys.stdin.readline().strip())
for i in range(N):
    name, g, y, s = sys.stdin.readline().split()
    g = int(g)
    y = int(y)
    s = int(s)
    arr.append([name, g, y, s])

arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(arr[i][0])