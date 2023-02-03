# 연속합

import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

seq_sum = [0] * n
# print(num)
# print(count)
seq_sum[0] = num[0]
for i in range(1, n):
    seq_sum[i] = max(seq_sum[i-1] + num[i], num[i])

print(max(seq_sum))