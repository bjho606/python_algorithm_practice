# 흙길 보수하기

import sys

input = sys.stdin.readline

N, L = map(int, input().split())

count = 0

pool_list = []
for i in range(N):
    start, end = map(int, input().split())
    pool_list.append((start, end))

pool_list.sort(key=lambda x: x[0])
# print(pool_list)

covered = -1
for start, end in pool_list:
    # 시간초과
    # for i in range(start, end):
    #     if covered < i:
    #         covered = i + L - 1
    #         count += 1
    #         i = covered

    if covered < start:
        length = end - start
    else:
        length = end - covered
    if length > 0:
        count += (length // L) + (1 if length % L != 0 else 0)
        covered = end + (L - (length % L) if length % L != 0 else 0)
    # print(length, covered)
    # print(count)

print(count)