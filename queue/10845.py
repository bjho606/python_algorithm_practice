# 큐

import sys

def push(arr, x):
    arr.append(x)

    return arr

def pop(arr):
    if len(arr) <= 0:
        print(-1)
        return arr

    val = arr[0]
    # del arr[0]
    arr.pop(0)
    print(val)

    return arr

def size(arr):
    print(len(arr))
    return

def empty(arr):
    print(1 if len(arr) <= 0 else 0)
    return

def front(arr):
    if len(arr) <= 0:
        print(-1)
    else:
        print(arr[0])

    return

def back(arr):
    if len(arr) <= 0:
        print(-1)
    else:
        print(arr[len(arr)-1])

    return

N = int(sys.stdin.readline())
arr = []

for n in range(N):
    com = sys.stdin.readline().split()
    
    if(com[0] == 'push'):
        push(arr, com[1])
    elif(com[0] == 'pop'):
        pop(arr)
    elif(com[0] == 'size'):
        size(arr)
    elif(com[0] == 'empty'):
        empty(arr)
    elif(com[0] == 'front'):
        front(arr)
    elif(com[0] == 'back'):
        back(arr)