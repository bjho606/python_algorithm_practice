# 부분합

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ps = [0]
for i in range(N):
    ps.append(ps[i] + arr[i])
# print(ps)

left, right = 0, 1
min_length = N
flag = False
while right <= N:
    if ps[right] - ps[left] < S:
        right += 1
    else:
        while left < right:
            left += 1
            if ps[right] - ps[left] < S:
                min_length = min(min_length, right - (left-1))
                # print(left, right)
                # left = right
                flag = True
                break

# ssum = 0
# while right <= N:
#     ssum += arr[right]

#     if ssum < S:
#         right += 1
#     else:
#         temp = ssum
#         while left < right:
#             left += 1
#             temp -= arr[left]
#             if temp < S:
#                 min_length = min(min_length, right - (left-1))
#                 left = right
#                 flag = True
#                 break

if flag:
    print(min_length)
else:
    print(0)