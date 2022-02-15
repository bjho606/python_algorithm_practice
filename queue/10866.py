# 덱 (Deque)

import sys

def push_front(arr, x):
    arr.insert(0, x)
    return arr

def push_back(arr, x):
    arr.append(x)
    return arr

def pop_front(arr):
    if len(arr) <= 0: 
        print(-1)
        return
    val = arr[0]
    arr.pop(0)
    print(val)
    return arr

def pop_back(arr):
    if len(arr) <= 0: 
        print(-1)
        return
    val = arr[len(arr)-1]
    arr.pop(len(arr)-1)
    print(val)
    return arr

def size(arr):
    print(len(arr))
    return

def empty(arr):
    print(1 if len(arr)<=0 else 0)
    return

def front(arr):
    if len(arr) <= 0: 
        print(-1)
        return
    print(arr[0])
    return

def back(arr):
    if len(arr) <= 0: 
        print(-1)
        return
    print(arr[len(arr)-1])
    return

N = int(sys.stdin.readline())
arr = []

for n in range(N):
    com = sys.stdin.readline().split()

    if(com[0] == 'push_back'):
        push_back(arr, com[1])
    if(com[0] == 'push_front'):
        push_front(arr, com[1])
    elif(com[0] == 'pop_front'):
        pop_front(arr)
    elif(com[0] == 'pop_back'):
        pop_back(arr)
    elif(com[0] == 'size'):
        size(arr)
    elif(com[0] == 'empty'):
        empty(arr)
    elif(com[0] == 'front'):
        front(arr)
    elif(com[0] == 'back'):
        back(arr)