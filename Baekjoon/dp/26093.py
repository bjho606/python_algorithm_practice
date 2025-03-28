# 고양이 목에 리본 달기

import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    
    joys = []
    dp = []

    for i in range(N):
        t = list(map(int, input().split()))
        joys.append(t)
        dp.append(t)

        if i == 0:
            continue
        
        sorted_t = sorted(dp[i-1], reverse=True)
        max1, max2 = sorted_t[0], sorted_t[1]

        for j in range(K):
            if joys[i-1][j] == max1:
                dp[i][j] = joys[i][j] + max2
            else:
                dp[i][j] = joys[i][j] + max1

    print(max(dp[N-1]))

if __name__ == "__main__":
    solution()