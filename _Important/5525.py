# IOIOI

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    M = int(input())
    S = input().rstrip()

    count = 0

    P = 'I' + 'OI' * N

    # 반점짜리 정답
    # for i, s in enumerate(S):
    #     if s == 'I':
    #         if i + p_len <= M:
    #             if S[i:i + p_len] == P:
    #                 count += 1

    p_len = N * 2 + 1
    left, right = 0, 0
    
    while right < M:
        if S[right:right+3] == 'IOI':
            right += 2
            if right - left + 1 == p_len:
                count += 1
                left += 2
        else:
            left = right = right + 1

    print(count)

if __name__ == "__main__":
    solution()