# 색종이 만들기

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))
    # print(paper)

    white, blue = 0, 0

    def divide(paper, length, x, y):
        nonlocal white, blue

        if length == 1:
            if paper[x][y] == 0:
                white += 1
            else:
                blue += 1
            return
        else:
            color = paper[x][y]

            for i in range(x, x + length):
                for j in range(y, y + length):
                    if paper[i][j] != color:
                        divide(paper, length // 2, x, y)
                        divide(paper, length // 2, x + length // 2, y)
                        divide(paper, length // 2, x, y + length // 2)
                        divide(paper, length // 2, x + length // 2, y + length // 2)
                        return

            if color == 0:
                white += 1
            else:
                blue += 1

    divide(paper, N, 0, 0)

    print(white)
    print(blue)

if __name__ == "__main__":
    solution()