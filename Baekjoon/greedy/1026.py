# 보물

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A)
sorted_B = sorted(B, reverse=True)

min_ans = 0
for i in range(N):
    min_ans += sorted_A[i] * sorted_B[i]

print(min_ans)