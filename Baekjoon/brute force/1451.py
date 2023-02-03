# 직사각형으로 나누기

import sys

def get_sum(x1, y1, x2, y2):
    # print(x1, y1, x2, y2)
    sum = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            sum += rec[i][j]
    
    # print(sum)
    return sum

N, M = map(int, sys.stdin.readline().split())
rec = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(N)]

max_ans = 0

# case1 : 세로만
for i in range(M-1):
    for j in range(i+1, M):
        # print(i, j)
        r1 = get_sum(0, 0, N-1, i)
        r2 = get_sum(0, i+1, N-1, j)
        r3 = get_sum(0, j+1, N-1, M-1)
        # print(r1+r2+r3)
        if r1 == 0 or r2 == 0 or r3 == 0: continue
        if max_ans < r1*r2*r3:
            max_ans = r1*r2*r3

# case2 : 가로만
for i in range(N-1):
    for j in range(i+1, N):
        r1 = get_sum(0, 0, i, M-1)
        r2 = get_sum(i+1, 0, j, M-1)
        r3 = get_sum(j+1, 0, N-1, M-1)
        if r1 == 0 or r2 == 0 or r3 == 0: continue
        if max_ans < r1*r2*r3:
            max_ans = r1*r2*r3

# case3 : 세1, 가2
for i in range(M):
    for j in range(N):
        r1 = get_sum(0, 0, N-1, i)
        r2 = get_sum(0, i+1, j, M-1)
        r3 = get_sum(j+1, i+1, N-1, M-1)
        if r1 == 0 or r2 == 0 or r3 == 0: continue
        if max_ans < r1*r2*r3:
            max_ans = r1*r2*r3

# case4 : 가2, 세1
for i in range(M):
    for j in range(N):
        r1 = get_sum(0, 0, j, i)
        r2 = get_sum(j+1, 0, N-1, i)
        r3 = get_sum(0, i+1, N-1, M-1)
        if r1 == 0 or r2 == 0 or r3 == 0: continue
        if max_ans < r1*r2*r3:
            max_ans = r1*r2*r3

# case5 : 가1, 세2
for i in range(N):
    for j in range(M):
        r1 = get_sum(0, 0, i, M-1)
        r2 = get_sum(i+1, 0, N-1, j)
        r3 = get_sum(i+1, j+1, N-1, M-1)
        if r1 == 0 or r2 == 0 or r3 == 0: continue
        if max_ans < r1*r2*r3:
            max_ans = r1*r2*r3

# case6 : 세2, 가1
for i in range(N):
    for j in range(M):
        r1 = get_sum(0, 0, i, j)
        r2 = get_sum(0, j+1, i, M-1)
        r3 = get_sum(i+1, 0, N-1, M-1)
        if r1 == 0 or r2 == 0 or r3 == 0: continue
        if max_ans < r1*r2*r3:
            max_ans = r1*r2*r3

print(max_ans)