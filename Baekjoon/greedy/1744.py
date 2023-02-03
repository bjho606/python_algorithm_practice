# 수 묶기

import sys

N = int(sys.stdin.readline())

positive = []
negative = []
sum = 0
for i in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        positive.append(num)
    elif num == 1:
        sum += num
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        sum += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive) - 1, 2):
        sum += positive[i] * positive[i+1]
    sum += positive[len(positive)-1]

if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        sum += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative) - 1, 2):
        sum += negative[i] * negative[i+1]
    sum += negative[len(negative)-1]

print(sum)