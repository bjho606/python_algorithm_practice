# 쿼드트리

import sys

def compress_img(img, x, y, length):
    # print('(', end='')

    temp = img[x][y]
    for i in range(x, x+length):
        for j in range(y, y+length):
            if img[i][j] != temp:
                print('(', end='')
                for k in range(2):
                    for l in range(2):
                        compress_img(img, x + k*length//2, y + l*length//2, length//2)

                print(')', end='')
                return

    print(temp, end='')

    # print(')', end='')

N = int(sys.stdin.readline())

img = [list(map(int, input())) for _ in range(N)]
# print(img)

compress_img(img, 0, 0, N)