# 알파벳 찾기

import sys

pos = [-1 for i in range(26)]
S = sys.stdin.readline().strip()

for i, letter in enumerate(S):
    asci = ord(letter)-ord('a')
    if pos[asci] == -1:
        pos[asci] = i

ans = str(pos)
ans = ans[1:-1].replace(',','')
print(ans)