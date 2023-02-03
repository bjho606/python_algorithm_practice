# 카드 구매하기

import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
# print(P)

card = P
# print(card)

for i in range(N):
    for j in range(i):
        # print(i, j)
        card[i] = max(card[i], card[j] + card[i-j-1])
        # print(card[i])

print(card[N-1])