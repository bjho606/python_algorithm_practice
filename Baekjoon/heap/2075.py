# N번쨰 큰 수

"""
메모리 제한이 굉장히 작다..!
배열의 크기를 최소한으로 줄이는게 포인트
크기 N의 배열을 유지하며, 정렬을 유지하는게 좋겠다..
"""

import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())

    board = list(map(int, input().split()))
    heapq.heapify(board)

    for _ in range(N-1):
        for num in list(map(int, input().split())):
            if (num > board[0]):
                heapq.heappushpop(board, num)
    # print(board)
    print(board[0])

if __name__ == "__main__":
    solution()