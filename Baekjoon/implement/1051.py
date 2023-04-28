# 숫자 정사각형

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rect = []
for i in range(N):
    row = list(map(int, input().rstrip()))
    rect.append(row)
# print(rect)

max_size = 0
for i in range(N):
    for j in range(M):
        for l in range(min(N,M)):
            # print(square_len)
            if i+l < N and j+l < M:
               if rect[i][j] == rect[i+l][j] == rect[i][j+l] == rect[i+l][j+l]:
                    size = (l+1)**2
                    max_size = max(max_size, size)

print(max_size)