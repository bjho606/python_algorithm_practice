# K번째 수

import sys

arr = []

N, K = map(int, sys.stdin.readline().split())
num = map(int, sys.stdin.readline().split())
arr += num

arr.sort()

print(arr[K-1])