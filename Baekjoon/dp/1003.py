# 피보나치 함수

import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())

        c0, c1 = 0, 0
        if N == 0:
            c0 = 1
        elif N == 1:
            c1 = 1
        else:
            c0, c1 = 1, 1
            for _ in range(1, N-1):
                c0, c1 = c1, c0+c1
            
        print(c0, c1)

if __name__ == "__main__":
    solution()