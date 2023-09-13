# 최소 힙

import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())

    heap = []

    for _ in range(N):
        x = int(input())

        if x == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, x)

if __name__ == "__main__":
    solution()