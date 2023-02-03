# 괄호

import sys

count = []
N = int(sys.stdin.readline())

for i in range(N):
    count.clear()
    flag = 0
    com = sys.stdin.readline().strip()
    for letter in com:
        # print(letter)
        if letter == '(':
            count.insert(0,letter)
        else:
            if len(count) <= 0:
                flag = 1
                print('NO')
                break
            count.pop(0)
    if len(count) > 0:
        print('NO')
        continue
    if flag == 0:
        print('YES')