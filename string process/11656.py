# 접미사 배열

import sys

S = sys.stdin.readline().strip()
arr = []

for i in range(len(S)):
    arr.append(S[i:])

arr.sort()
# print(arr)

for word in arr:
    print(word)