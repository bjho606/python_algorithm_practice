# 구간 합 구하기 4

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
ps = [0, nums[0]]
for idx in range(1, N):
    ps.append(ps[idx] + nums[idx])
print(ps)

for _ in range(M):
    i, j = map(int, input().split())
    print(ps[j] - ps[i-1])