# 점프왕 쩰리 (small)

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

dx = [0, 1]
dy = [1, 0]

def solution():
    N = int(input())
    maps = []
    for i in range(N):
        maps.append(list(map(int, input().split())))
    # print(maps)
        
    def dfs(x, y):
        isPossible = False
 
        if maps[x][y] == -1:
            return True
        if maps[x][y] == 0:
            return False

        for d in range(2):
            nextX = x + dx[d]*maps[x][y]
            nextY = y + dy[d]*maps[x][y]

            if nextX >= N or nextY >= N: continue
            isPossible = dfs(nextX, nextY)

            if isPossible: break

        return isPossible

    result = dfs(0,0)

    if result:
        print('HaruHaru')
    else:
        print('Hing')

if __name__ == "__main__":
    solution()