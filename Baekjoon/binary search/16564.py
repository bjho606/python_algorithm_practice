# 히오스 프로게이머

import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    levels = [0 for _ in range(N)]
    for i in range(N):
        levels[i] = int(input())
    # print(levels)

    T = 0
    start = min(levels)
    end = max(levels) + K

    while start <= end:
        targetLevel = (start + end) // 2

        diff_sum = 0
        for level in levels:
            if targetLevel > level:
                diff_sum += (targetLevel - level)
        
        if diff_sum > K:
            end = targetLevel - 1
        elif diff_sum <= K:
            start = targetLevel + 1
            T = max(T, targetLevel)

    print(T)

if __name__ == "__main__":
    solution()