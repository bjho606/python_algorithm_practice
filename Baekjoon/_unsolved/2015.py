# 다시.. 시간초과 안나게..
# 수들의 합 4
# prefix sum

from itertools import combinations
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

A = [0] + list(map(int, input().split()))

psum = [0] * (N+1)
for i in range(1, N+1):
    psum[i] = psum[i-1] + A[i]
print(psum)

# 시간초과
# count = 0
# count += A.count(K)
# if K == 0:
#     count -= 1
# for combi_index in combinations(range(1, N+1), 2):
#     temp_sum = psum[combi_index[1]] - psum[combi_index[0]-1]
#     if temp_sum == K:
#         # print(combi_index)
#         count += 1
# print(count)

count = {}
ans = 0
