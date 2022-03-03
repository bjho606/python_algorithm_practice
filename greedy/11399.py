# ATM

import sys

N = int(sys.stdin.readline())

P = list(map(int, sys.stdin.readline().split()))
P.sort()

min_time = 0
for i in range(N):
    min_time += P[i] * (N-i)

print(min_time)