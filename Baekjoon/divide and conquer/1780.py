# 종이의 개수

import sys

def dq(arr, x, y, length):
    global mo, z, o

    temp = arr[x][y]

    for i in range(x, x+length):
        for j in range(y, y+length):
            if arr[i][j] != temp:
                for k in range(3):
                    for l in range(3):
                        dq(arr, x + k * length//3, y + l * length//3, length//3)

                return

    if temp == -1:
        mo += 1
    elif temp == 0:
        z += 1
    elif temp == 1:
        o += 1
    return

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# print(arr)
mo, z, o = 0, 0, 0

dq(arr, 0, 0, len(arr[0]))
print(mo)
print(z)
print(o)