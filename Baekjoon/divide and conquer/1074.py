# Z

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    N, r, c = map(int, input().split())

    def divide(y, x, n):
        nonlocal count
        if n == 0:
            return
        
        n -= 1

        # 1구역
        if x < 2**n and y < 2**n:
            count += (2**n) * (2**n) * 0
            divide(y, x, n)

        # 2구역
        elif x >= 2**n and y < 2**n:
            count += (2**n) * (2**n) * 1
            divide(y, x - 2**n, n)

        # 3구역
        elif x < 2**n and y >= 2**n:
            count += (2**n) * (2**n) * 2
            divide(y - 2**n, x, n)

        # 4구역
        else:   # x >= 2**n and y >= 2**n
            count += (2**n) * (2**n) * 3
            divide(y - 2**n, x - 2**n, n)

    count = 0

    divide(r, c, N)

    print(count)

if __name__ == "__main__":
    solution()