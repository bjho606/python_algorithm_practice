# 괄호의 값 (다시 해보기)
# data structure

import sys
input = sys.stdin.readline

word_stack = []
calc_stack = []
ans = 0
temp = 1

ip = input().strip()
for idx, word in enumerate(ip):
    if word == '(':
        word_stack.append(word)
        temp *= 2
    elif word == '[':
        word_stack.append(word)
        temp *= 3
    elif word == ')':
        if not word_stack or word_stack[-1] == '[':
            ans = 0
            break
        if ip[idx-1] == '(':
            ans += temp
        
        word_stack.pop()
        temp //= 2
    elif word == ']':
        if not word_stack or word_stack[-1] == '(':
            ans = 0
            break
        if ip[idx-1] == '[':
            ans += temp

        word_stack.pop()
        temp //= 3

if word_stack:
    print(0)
else:
    print(ans)