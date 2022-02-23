# 숫자 카드

import sys

def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            print(1, end=' ')
            return
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1

    print(0, end=' ')
    return

N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
check = list(map(int, sys.stdin.readline().split()))
cards.sort()

# 시간초과
# for i in range(len(check)):
#     if check[i] in cards:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

for target in check:
    binary_search(cards, 0, len(cards)-1, target)