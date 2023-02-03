# 동물원

import sys

N = int(sys.stdin.readline())

lion = [[0,0,0] for _ in range(N)]
lion[0][0] = 1  # no lion
lion[0][1] = 1  # left lion
lion[0][2] = 1  # right lion

for i in range(1, N):
    lion[i][0] = (lion[i-1][0] + lion[i-1][1] + lion[i-1][2]) % 9901
    lion[i][1] = (lion[i-1][0] + lion[i-1][2]) % 9901
    lion[i][2] = (lion[i-1][0] + lion[i-1][1]) % 9901

print(sum(lion[N-1]) % 9901)