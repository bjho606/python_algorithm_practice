# 스택

import sys

def push(arr, x):
    arr.insert(0, x)

    return arr

def pop(arr):
    if len(arr) <= 0:
        print(-1)
        return
    print(arr[0])
    arr.pop(0)
    return arr

def size(arr):
    print(len(arr))
    return

def empty(arr):
    print(1 if len(arr) <= 0 else 0)
    return

def top(arr):
    if len(arr) <= 0:
        print(-1)
        return
    print(arr[0])
    return

arr = []
N = int(sys.stdin.readline())

for i in range(N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        push(arr, com[1])
    elif com[0] == 'pop':
        pop(arr)
    elif com[0] == 'size':
        size(arr)
    elif com[0] == 'empty':
        empty(arr)
    elif com[0] == 'top':
        top(arr)