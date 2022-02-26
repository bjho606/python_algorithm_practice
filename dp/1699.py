# 제곱수의 합

import sys

N = int(sys.stdin.readline())

count = [i for i in range(N+1)]

for i in range(1, N+1):
    # count[i] = i
    for j in range(1, i):
        if j*j > i:
            break
        # if j*j == i:
        #     count[i] = 1
        if count[i] > count[i-j*j] + 1:
            count[i] = count[i-j*j] + 1

print(count[N])