# 알파벳 개수

import sys

count = [0 for i in range(26)]
S = sys.stdin.readline().strip()

for letter in S:
    asci = ord(letter)-ord('a')
    count[asci] += 1

ans = str(count)
ans = ans[1:-1].replace(',','')
print(ans)