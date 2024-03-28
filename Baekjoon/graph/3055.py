# 탈출

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution():
    R, C = map(int, input().split())
    
    def printArr(arr):
        for i in range(R):
            print(arr[i])
        print()

    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    waters = []
    dist = [[0]*C for _ in range(R)]

    forrest = []
    for i in range(R):
        temp = list(input().rstrip())
        forrest.append(temp)
    # print(forrest)
        
    for i in range(R):
        for j in range(C):
            if forrest[i][j] == 'S':
                start_x, start_y = i, j
            elif forrest[i][j] == 'D':
                end_x, end_y = i, j
            elif forrest[i][j] == '*':
                waters.append((i,j))

    ans = 0
    q = deque()
    q.append((start_x, start_y))
    for water_coord in waters:
        q.append(water_coord)
    # print(q)
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if nx<0 or nx>=R or ny<0 or ny>=C: continue

            # 고슴도치인 경우
            if forrest[x][y] == 'S':
                if forrest[nx][ny] == '*' or forrest[nx][ny] == 'S' or forrest[nx][ny] == 'X': continue
                if nx == end_x and ny == end_y:
                    print(dist[x][y] + 1)
                    exit()
                
                forrest[nx][ny] = 'S'
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

            # 물인 경우
            elif forrest[x][y] == '*':
                if forrest[nx][ny] == '*' or forrest[nx][ny] == 'X' or forrest[nx][ny] == 'D': continue

                forrest[nx][ny] = '*'
                q.append((nx, ny))
        # printArr(forrest)
    print('KAKTUS')

if __name__ == "__main__":
    solution()