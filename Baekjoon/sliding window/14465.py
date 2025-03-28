# 소가 길을 건너간 이유 5

import sys
input = sys.stdin.readline

def solution():
    N, K, B = map(int, input().split())
    broken = [0]*N

    for i in range(B):
        t = int(input())
        broken[t-1] = 1
    # print(broken)

    answer = 100000
    fix_count = 0
    for i in range(K):
        if broken[i]:
            fix_count += 1
    answer = fix_count

    for i in range(K, N):
        if broken[i]:
            fix_count += 1
        if broken[i-K]:
            fix_count -= 1
        answer = min(answer, fix_count)

    print(answer)

if __name__ == "__main__":
    solution()