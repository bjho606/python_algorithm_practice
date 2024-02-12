# 1로 만들기 2

import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    dp = [0] * (N+1)
    process = [[1] for _ in range(N+1)]

    for i in range(2, N+1):
        # case 1. dp[이전값] + 1 로 현재값 초기화
        dp[i] = dp[i-1] + 1
        process[i] = process[i-1] + [i]

        # case 2. (3으로 나누어질 경우) 현재 값 vs dp[//3]
        if i % 3 == 0:
            if min(dp[i//3], dp[i] - 1) == dp[i//3]:
                dp[i] = dp[i//3] + 1
                process[i] = process[i//3] + [i]
        # case 3. (2로 나누어질 경우) 현재 값 vs dp[//2]
        if i % 2 == 0:
            if min(dp[i//2], dp[i] - 1) == dp[i//2]:
                dp[i] = dp[i//2] + 1
                process[i] = process[i//2] + [i]
    # print(dp)

    print(dp[N])
    print(*reversed(process[N]))

if __name__ == "__main__":
    solution()