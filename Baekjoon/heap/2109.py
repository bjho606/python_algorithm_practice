# 순회강연

"""
(100, 3), (90, 1), (5, 2), (25, 2)
(90, 1), (25, 2), (5, 2), (100, 3)

(50, 2), (10, 1), (40, 2), (30, 1)
(30, 1), (50, 2), (40, 2)

"""

import sys
import heapq
input = sys.stdin.readline

def solution():
    n = int(input())

    lecture_info = []

    for i in range(n):
        p, d = map(int, input().split())
        lecture_info.append((p, d))
    
    lecture_info.sort(key=lambda x: (x[1], -x[0]))
    # print(lecture_info)

    heap = []
    ans = 0
    for i in range(n):
        p, d = lecture_info[i]
        
        heapq.heappush(heap, p)

        if len(heap) > d:
            heapq.heappop(heap)
    # print(heap)

    ans = sum(heap)
    print(ans)

if __name__ == "__main__":
    solution()