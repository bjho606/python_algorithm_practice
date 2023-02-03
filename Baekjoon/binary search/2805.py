# 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start+end) // 2
    count = 0
    for tree in trees:
        dif = tree - mid
        if dif >= 0:
            count += dif
    
    if count >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)