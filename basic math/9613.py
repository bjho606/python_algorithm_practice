# 최대공약수의 합

import sys

def gcd(a, b):
    n1 = max(a, b)
    n2 = min(a, b)
    while(n2 != 0):
        temp = n1 % n2
        n1 = n2
        n2 = temp

    return n1

t = int(input())

for i in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    n = arr[0]
    sum = 0

    for i in range(1, n):
        for j in range(i+1, n+1):
            sum += gcd(arr[i], arr[j])
    
    print(sum)