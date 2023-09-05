# 유기농 배추

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(field, visited, x, y):
    visited[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= len(field) or ny < 0 or ny >= len(field[0]):
            continue
        if visited[nx][ny]:
            continue
        
        if field[nx][ny] == 1:
            dfs(field, visited, nx, ny)

    return visited

def solution():
    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())

        field = [[0 for _ in range(M)] for _ in range(N)]
        visited = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            X, Y = map(int, input().split())
            field[Y][X] = 1
        
        count = 0

        for i in range(N):
            for j in range(M):
                if not visited[i][j] and field[i][j] == 1:
                    count += 1
                    visited = dfs(field, visited, i, j)
        
        print(count)

if __name__ == "__main__":
    solution()