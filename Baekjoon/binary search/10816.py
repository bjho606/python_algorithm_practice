# 숫자 카드 2

import sys

def binary_search(arr, start, end, target):
    count = 0
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            count = card_dic[target]
            break

    return count

N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
check = list(map(int, sys.stdin.readline().split()))
cards.sort()

card_dic = {}
for card in cards:
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1

for target in check:
    print(binary_search(cards, 0, len(cards)-1, target), end=' ')