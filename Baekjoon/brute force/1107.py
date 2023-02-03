# 리모컨

import sys

target = int(sys.stdin.readline().strip())
available = {str(i) for i in range(10)}
N = int(sys.stdin.readline().strip())
if N != 0:
    broken = set(sys.stdin.readline().split())
    available -= broken

min_count = abs(100 - target)

for num in range(1000001):
    num = str(num)

    for i in range(len(num)):
        if num[i] not in available:
            break
        if i == len(num) - 1:
            min_count = min(min_count, abs(target - int(num)) + len(num))

print(min_count)