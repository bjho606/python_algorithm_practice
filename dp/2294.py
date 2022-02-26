# 동전2

import sys

n, k = map(int, sys.stdin.readline().split())

coin = [0]
count = [-1] * (k+1)
for i in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort()
# print(coin)
# print(count)
for i in range(coin[1], k+1):
    temp = 100000
    for j in range(n, 0, -1):
        # print(i, j, coin[j], count[i])
        if i == coin[j]: 
            count[i] = 1
            break
        if i - coin[j] < 0:
            continue
        if count[i - coin[j]] != -1:
            count[i] = min(temp, count[i-coin[j]]+1)
            temp = count[i]
    # print(i , ":", count[i])

print(count[k])