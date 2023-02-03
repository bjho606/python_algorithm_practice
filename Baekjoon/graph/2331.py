# 반복 수열

import sys

input = sys.stdin.readline

A, P = map(int, input().split())

D = [A]
count = 0
ans = 0

while True:
    length = len(str(D[count]))
    next_num = 0
    for i in range(length):
        next_num += int(str(D[count])[i]) ** P
    # print(next_num)
    if next_num in D:
        ans = D.index(next_num)
        
        break
    else:
        D.append(next_num)
    # print(count, D)
    count += 1

print(ans)