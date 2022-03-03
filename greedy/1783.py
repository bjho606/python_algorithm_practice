# 병든 나이트

import sys

N, M = map(int, sys.stdin.readline().split())

count = 0

if N == 1 or M == 1:
    print(1)
    exit()
elif N == 2:
    count += min(4, (M-1)//2 + 1)
elif M <= 6:
    count += min(4, M)
else:
    count += M-2

print(count)