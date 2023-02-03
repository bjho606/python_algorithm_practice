from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))

sum_list = []

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

for cases in combinations(H, M):
    # print(cases)
    sum_temp = 0
    for item in cases:
        sum_temp += item
    
    if isPrime(sum_temp):
        if sum_temp not in sum_list:
            sum_list.append(sum_temp)

if len(sum_list) <= 0:
    print(-1)
else:
    sum_list.sort()
    print(*sum_list)