# 가장 가까운 두 점 (다시)
# divide and conquer

import sys

n = int(sys.stdin.readline())
point = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
point.sort()

# print(point)