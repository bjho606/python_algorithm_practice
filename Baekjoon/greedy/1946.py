# 신입 사원

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    ls = []

    for i in range(N):
        score1, score2 = map(int, input().split())
        ls.append([score1, score2])

    ls.sort(key=lambda x: x[0])
    count = 1
    max_limit = ls[0][1]

    for i in range(1, N):
        if ls[i][1] < max_limit:
            max_limit = ls[i][1]
            count += 1
        
    print(count)