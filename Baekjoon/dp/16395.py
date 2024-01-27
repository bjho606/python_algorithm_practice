# 파스칼의 삼각형

import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())

    dp = [[1], [1,1]]

    for i in range(2, n+1):
        pas = [1]
        for j in range(i-1):
            pas.append(dp[i-1][j] + dp[i-1][j+1])
        pas.append(1)

        dp.append(pas)
    
    print(dp[n-1][k-1])

if __name__ == "__main__":
    solution()