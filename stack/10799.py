# 쇠막대기

import sys

ans = 0
arr = []
given = sys.stdin.readline().strip()

for i, letter in enumerate(given):
    if letter == '(':
        arr.append(letter)
    else:
        if given[i-1] == '(':
            arr.pop()
            ans += arr.count('(')
        else:
            arr.pop()
            ans += 1

print(ans)