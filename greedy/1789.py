# 수들의 합
import sys

input = sys.stdin.readline

S = int(input())

sums = 0
N = 0

while True:
    if sums > S:
        N -= 1
        break
    elif sums == S:
        break

    N += 1
    sums += N

print(N)