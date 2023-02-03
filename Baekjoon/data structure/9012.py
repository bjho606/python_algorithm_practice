# 괄호

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
q = deque()
for i in range(T):
    flag = 0
    q.clear()
    com = input().strip()
    for letter in com:
        if letter == '(':
            q.append(letter)
        else:
            if len(q) <= 0:
                flag = 1
                break
            q.pop()
    if len(q) > 0 or flag == 1:
        print('NO')
    else:
        print('YES')