# [카드 정렬하기]

import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())

    cards = []
    for i in range(N):
        heapq.heappush(cards, int(input()))
    
    min_sum = 0
    if len(cards) == 1:
        print(0)
    else:
        while len(cards) > 1:
            cur_sum = heapq.heappop(cards) + heapq.heappop(cards)
            min_sum += cur_sum
            heapq.heappush(cards, cur_sum)

        print(min_sum)

if __name__ == "__main__":
    solution()