# Road Reconstruction

"""
[아이디어]
1. 백트랙킹..?
2. 그냥 백트랙킹만 하면 안되고, 해당 좌표까지 간 최소 cost를 저장하고 확인 & 갱신
--- 백트랙킹 방식으로 하면 메모리 초과..?
3. 지나온 좌표를 여러번 거치지 않고, 가장 적은 비용으로 한번만 방문하기 위해 heap으로..!
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution():
    m, n = map(int, input().split())

    board = []
    for i in range(m):
        board.append(list(map(int, input().split())))
    
    minVisited = [[INF]*n for _ in range(m)]
    minVisited[0][0] = board[0][0]
    minCost = -1

    pq = []
    heapq.heappush(pq, [minVisited[0][0], (0, 0)])

    while pq:
        curCost, coords = heapq.heappop(pq)
        cx, cy = coords
        # print(cx, cy, curCost)
        if curCost == -1: break
        if cx == m-1 and cy == n-1:
            minCost = curCost
            break

        if curCost > minVisited[cx][cy]: continue

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]

            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if board[nx][ny] == -1: continue

            nextCost = curCost + board[nx][ny]
            if minVisited[nx][ny] <= nextCost: continue

            minVisited[nx][ny] = nextCost
            heapq.heappush(pq, [nextCost, (nx, ny)])

    # [메모리 초과]
    # def backtrack(x, y, cost):
    #     global minCost, minVisited
    #     # print(x, y)
    #     if board[x][y] == -1:
    #         return

    #     cost += board[x][y]

    #     if x == m-1 and y == n-1:
    #         minCost = min(minCost, cost)
    #         # print(minVisited)
    #         # print(minCost)
    #         return

    #     for d in range(4):
    #         nx, ny = x + dx[d], y + dy[d]

    #         if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
    #         # if minVisited[nx][ny]: continue
    #         if board[nx][ny] == -1: continue

    #         if cost + board[nx][ny] >= minVisited[nx][ny]: continue

    #         minVisited[nx][ny] = cost + board[nx][ny]
    #         backtrack(nx, ny, cost)
    
    # backtrack(0, 0, 0)

    print(minCost)


if __name__ == "__main__":
    solution()