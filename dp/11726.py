# 2xn 타일링

import sys

n = int(sys.stdin.readline())

tile = [0,1,2]

for i in range(3, n+1):
    tile.append(tile[i-1] + tile[i-2])

print(tile[n]%10007)