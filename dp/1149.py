# RGB 거리

import sys

N = int(sys.stdin.readline())
r = [0] * N
g = [0] * N
b = [0] * N
houses = []
for i in range(N):
    houses.append(list(map(int, sys.stdin.readline().split())))

r[0] = houses[0][0]
g[0] = houses[0][1]
b[0] = houses[0][2]

# print(houses)
for i in range(1, N):
    r[i] = min(g[i-1], b[i-1]) + houses[i][0]
    g[i] = min(b[i-1], r[i-1]) + houses[i][1]
    b[i] = min(r[i-1], g[i-1]) + houses[i][2]

print(min(r[N-1], g[N-1], b[N-1]))