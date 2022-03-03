# 30

import sys

num = list(map(int, sys.stdin.readline().rstrip('\n')))
num.sort()
check = sum(num)
if check % 3 != 0 or num[0] != 0:
    print(-1)
    exit()

for i in reversed(num):
    print(i, end='')