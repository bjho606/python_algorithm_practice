# 피보나치 수

import sys

n = int(sys.stdin.readline())

pibo = [0, 1]
for i in range(2, n+1):
    pibo.append(pibo[i-2] + pibo[i-1])

print(pibo[n])