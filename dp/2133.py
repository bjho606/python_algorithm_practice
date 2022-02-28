# 타일 채우기 (다시)

import sys

N = int(sys.stdin.readline())

tile = [0 for _ in range(N+1)]
tile[0] = 1
tile[1] = 0
if N >= 2:
    tile[2] = 3
# tile[3] = 0
# tile[4] = 11    # 3*3 + 2

for i in range(4, N+1, 2):
    tile[i] = tile[i-2] * 3

    for j in range(4, i+1, 2):
        tile[i] += tile[i-j] * 2

print(tile[N])