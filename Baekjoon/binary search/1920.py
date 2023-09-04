# 수 찾기

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    Ms = list(map(int, input().split()))

    A.sort()

    def binary_search(A, m):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == m:
                return True
            elif A[mid] < m:
                left = mid + 1
            else:
                right = mid - 1
        return False

    for m in Ms:
        if binary_search(A, m):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    solution()