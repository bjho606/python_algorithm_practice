# 카드 (가장 많이 가지고 있는 숫자)

import sys

arr = []
dic = {}
N = int(sys.stdin.readline().strip())
for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(dic[0][0])