# 1로 만들기

import sys

N = int(sys.stdin.readline())

count = [0, 0]
for i in range(2, N+1):
    case = count[i-1] + 1
    if i % 3 == 0 and i % 2 != 0:
        case = min(case, count[i//3] + 1)
    elif i % 2 == 0 and i % 3 != 0:
        case = min(case, count[i//2] + 1)
    elif i % 3 == 0 and i % 2 == 0:
        case = min(case, count[i//3] + 1, count[i//2] + 1)

    count.append(case)

print(count[N])