# 최고의 팀 만들기

"""
dp[N][i][j] : 1~N 까지 사람들 중, 백 i명, 흑 j명을 뽑았을 때의 최대값
dp[N][i][j] = max(dp[N-1][i][j], dp[N-1][i-1][j] + icost, dp[N-1][i][j-1] + jcost)
"""

import sys
input = sys.stdin.readline

def solution():
    abilities = [[0,0]]
    
    while True:
        try:
            a, b = map(int, input().split())
            abilities.append([a, b])
        except:
            break

    # print(abilities)
    
    N = len(abilities) - 1

    dp = [[[0]*(16) for _ in range(16)] for _ in range(N+1)]
    # print(dp)

    for i in range(1, N+1):
        for j in range(16):
            for k in range(16):
                dp[i][j][k] = dp[i-1][j][k]
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + abilities[i][0])
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + abilities[i][1])
                
    print(dp[N][15][15])

if __name__ == "__main__":
    solution()