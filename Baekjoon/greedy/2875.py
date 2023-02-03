# 대회 or 인턴

import sys

N, M, K = map(int, sys.stdin.readline().split())

count = 0

while N >= 2 and M >= 1 and N + M >= K + 3:
    N -= 2
    M -= 1
    count += 1

# 다른 풀이
# count += min(N//2, M)
# K -= N + M - count*3

# if K > 0:
#     count -= K//3
#     if K%3 != 0:
#         count -= 1

print(count)