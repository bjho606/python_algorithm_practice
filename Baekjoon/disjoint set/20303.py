# 할로윈의 양아치

import sys
input = sys.stdin.readline
"""
1. 연결된 아이들을 찾기 위해 union-find 를 사용 -> 최적화 (경로 압축, 제일 작은 노드로 부모 설정)
2. 연결된 아이들 그룹들 각각의 (인원수, 사탕 개수 총합) 구하기
3. 해당 그룹을 뽑느냐 마느냐의 knapsack 문제
"""

def find(x):
    if parent[x] == x: return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    rootX, rootY = find(x), find(y)

    parent[max(rootX, rootY)] = min(rootX, rootY)

N, M, K = map(int, input().split())

candies = [0] + list(map(int, input().split()))

parent = [i for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())

    union(a, b)

# print(parent)

candy_count = [0] * (N+1)
friend_count = [0] * (N+1)
for i in range(1, N+1):
    p = find(i)
    candy_count[p] += 1
    friend_count[p] += candies[i]
# print(candy_count)
# print(friend_count)

records = []
for i in range(1, N+1):
    if candy_count[i] == 0: continue
    records.append([candy_count[i], friend_count[i]])
# print(records)

dp = [[0]*K for _ in range(len(records))]

for i in range(len(records)):
    fcount, ccount = records[i]
    if i == 0:
        for cur_count in range(K):
            if cur_count >= fcount:
                dp[i][cur_count] = max(dp[i][cur_count], ccount)
    else:
        for cur_count in range(K):
            if cur_count >= fcount:
                dp[i][cur_count] = max(dp[i-1][cur_count], dp[i-1][cur_count-fcount] + ccount)
            else:
                dp[i][cur_count] = dp[i-1][cur_count]
# for i in range(len(records)):
#     print(dp[i])
print(dp[len(records)-1][K-1])

# [시간초과]
# visited = [0]*len(candies)
# totalCandy = 0

# def backtrack_group(x, pcount, ccount):
#     nonlocal totalCandy
#     if pcount < K:
#         totalCandy = max(totalCandy, ccount)

#     for group in record.keys():
#         if visited[group]: continue
#         if pcount + counts[group] >= K: continue
#         visited[group] = 1
#         backtrack_group(group, pcount + counts[group], ccount + record[group])
#         visited[group] = 0

# backtrack_group(0, 0, 0)
# print(totalCandy)
