# 하노이 탑 이동 순서

import sys

def hanoi(piece, start, end):
    if piece == 1:
        print(start, end)
        return

    hanoi(piece-1, start, 6-start-end)
    print(start, end)
    hanoi(piece-1, 6-start-end, end)

    return

N = int(sys.stdin.readline())

print(2**N - 1)

hanoi(N, 1, 3)