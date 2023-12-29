# 두개의 숫자열 (완전탐색)

import sys
input = sys.stdin.readline
import math

T = int(input())
for test_case  in range(1, T+1):
    N, M = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    len_A = len(A)
    len_B = len(B)

    llen = 0
    slen = 0

    if len_A >= len_B:
        longer = A
        shorter = B
        llen = len_A
        slen = len_B
    else:
        longer = B
        shorter = A
        llen = len_B
        slen = len_A

    answer = -math.inf
    for start_i in range(llen-slen+1):
        sums = 0
        for i in range(slen):
            sums += shorter[i] * longer[start_i + i]
        
        answer = max(answer, sums)
    
    print(f'#{test_case} {answer}')
