# 균형 잡힌 세상

import sys
input = sys.stdin.readline

while True:
    line = input().rstrip('\n')
    if line == '.':
        break

    flag = True
    stack = []

    for word in line:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
        elif word == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            else:
                stack.pop()

    if flag and not stack:
        print('yes')
    else:
        print('no')