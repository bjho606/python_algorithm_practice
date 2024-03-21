# 사회망 서비스 (SNS)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
[아이디어]
무조건 인접한 애 중 한명은 adapter
dp[node] : leaf에서부터 node 까지의 최소 어답터 수
dp[cur] = dp[next] 가 어답터인 경우, dp[next] 가 어답터가 아닌 경우 + 1
0 : not adapter
1 : adapter
dp[cur][0] => dp[next][1]                   -> 무조건 
dp[cur][1] => dp[next][0] vs dp[next][1]    -> 선택
"""

def solution():
    N = int(input())

    graph = [[] for _ in range(N)]

    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    def dfs(cur):
        nonlocal visited, dp
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                dfs(next)
                dp[cur][0] += dp[next][1]
                dp[cur][1] += min(dp[next][0], dp[next][1])

    ans = N

    # for start in range(N):
    visited = [0] * N
    dp = [[0,1] for _ in range(N)]
    visited[0] = 1
    dfs(0)

    ans = min(dp[0][0], dp[0][1])
    
    print(ans)

if __name__ == "__main__":
    solution()