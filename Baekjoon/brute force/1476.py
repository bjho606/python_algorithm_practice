# 날짜 계산

import sys

E, S, M = map(int, sys.stdin.readline().split())
count = 0

while True:
    if E == S == M:
        count += E
        break

    if E <= 1:
        E = 15
    else:
        E -= 1
    
    if S <= 1:
        S = 28
    else:
        S -= 1

    if M <= 1:
        M = 19
    else:
        M -= 1

    count += 1

print(count)