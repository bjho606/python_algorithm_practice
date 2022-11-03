# Byte Coin

import sys

input = sys.stdin.readline

n, w = map(int, input().split())
stock = []
for i in range(n):
    stock.append(int(input()))

coin = 0
for i in range(n-1):
    # 내일 더 오른다면
    if stock[i] < stock[i+1]:
        # 당장 살 수 있다면 산다
        if stock[i] <= w:
            coin = w//stock[i]
            w -= stock[i] * coin
    # 내일 더 떨어진다면 다 판다
    elif stock[i] > stock[i-1]:
        w += stock[i] * coin
        coin = 0
    
    # print(coin, w)
w += stock[n-1] * coin

print(w)