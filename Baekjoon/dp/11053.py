# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

# N < 1000 이므로 1초 -> N^2으로 풀어도 될듯
# 앞으로 전진하면서, 이전 값들과 비교하면서 최고점 + 1이 가능한지 확인

def solution():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [1 for _ in range(N)]
    # dp[0] = A[0]
    max_len = 1

    for i in range(1, N):                       # 앞으로 전진하면서
        for j in range(i):                      # 이전 모든 값들에서
            if A[i] > A[j]:                     # 자신보다 작은 값 중,
                dp[i] = max(dp[i], dp[j] + 1)   # 이전에 작았던 값들 + 1 vs 현재 자신보다 작은 값 + 1
    # print(dp)
    print(max(dp))

if __name__ == "__main__":
    solution()