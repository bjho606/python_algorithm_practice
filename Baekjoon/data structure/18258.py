# 큐2

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(N):
    com = input().split()
    # print(com)

    if com[0] == 'push':
        q.append(com[1])
    elif com[0] == 'pop':
        if len(q) <= 0:
            print(-1)
        else:
            print(q.popleft())
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if len(q) <= 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(q) <= 0:
            print(-1)
        else:
            print(q[0])
    elif com[0] == 'back':
        if len(q) <= 0:
            print(-1)
        else:
            print(q[-1])
