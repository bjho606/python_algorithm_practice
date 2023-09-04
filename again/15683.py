# 감시

import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

type = {
    1 : [[0],[1],[2],[3]],
    2 : [[0,1],[2,3]],
    3 : [[0,2],[0,3],[1,2],[2,3]],
    4 : [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    5 : [[0,1,2,3]]
}

N, M = map(int, input().split())
answer = N * M
office = []
for i in range(N):
    row = list(map(int, input().split()))
    office.append(row)
# print(office)

visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if office[i][j] != 0:
            visited[i][j] = -1
            answer -= 1
# print(visited)
# print(answer)

cctvs = []
for i in range(N):
    for j in range(M):
        if 1<= office[i][j] <= 5:
            cctv_num = office[i][j]
            cctvs.append((j,i,cctv_num))
# print(cctvs)



def dfs(cctv_count):
    if cctv_count == len(cctvs):
        answer = min(answer, blindspots)
        return
    else:
        

dfs(0)

# max_coverage = 0

# for cctv_info in cctvs:
#     x, y, cctv_num = cctv_info

# answer -= max_coverage

print(answer)