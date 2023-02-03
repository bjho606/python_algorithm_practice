# 집합

import sys
input = sys.stdin.readline

S = set()

def add(x):
    global S
    if x not in S:
        S.add(x)

def remove(x):
    global S
    if x in S:
        S.remove(x)

def check(x):
    global S
    if x in S:
        print(1)
    else:
        print(0)

def toggle(x):
    global S
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def all():
    global S
    S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

def empty():
    global S
    S = set()

M = int(input())

for i in range(M):
    given = input().rstrip()

    com, num = '', 0
    if len(given.split()) > 1:
        com, num = given.split()
    else:
        com = given

    if com == 'add':
        add(int(num))
    elif com == 'remove':
        remove(int(num))
    elif com == 'check':
        check(int(num))
    elif com == 'toggle':
        toggle(int(num))
    elif com == 'all':
        all()
    elif com == 'empty':
        empty()