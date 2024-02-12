# 나무 자르기

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    trees = list(map(int, input().split()))

    start = 0
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2

        cut = 0
        for i in range(N):
            if trees[i] > mid:
                cut += trees[i] - mid
        
        if cut >= M:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

if __name__ == "__main__":
    solution()