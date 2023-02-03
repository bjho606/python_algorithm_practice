# 별 찍기 10 (다시)
# divide and conquer

import sys

def star(N, x, y):
    if N == 1:
        return
    for i in range(x, x+N):
        for j in range(y, y+N):
            if x + N//3 <= i < x + 2*N//3 and y + N//3 <= j < y + 2*N//3:
                print(' ', end='')

            elif i % 3 == 0 and j % 3 == 0:
                for k in range(3):
                    for l in range(3):
                        star(N//3, i + k*N//3, j + l*N//3)

            else:
                print('', end='')
        print()

N = int(sys.stdin.readline())

star(N, 0, 0)

# for i in range(3):
#     for j in range(3):
#         if 1 <= i < 2 and 1 <= j < 2:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()