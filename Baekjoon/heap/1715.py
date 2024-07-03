# 카드 정렬하기

import heapq
import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    cards = []
    for i in range(N):
        card = int(input())
        heapq.heappush(cards, card)

    count = 0

    while len(cards) > 1:
        next_sum = heapq.heappop(cards) + heapq.heappop(cards)

        count += next_sum

        heapq.heappush(cards, next_sum)

    print(count)

if __name__ == "__main__":
    solution()