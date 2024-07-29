# 냅색 개념..
# 최고의 팀 만들기

"""
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