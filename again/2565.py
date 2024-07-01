# LIS - 원리를 잘 생각해내보자!
# 전깃줄

import sys
input = sys.stdin.readline

def solution():
    num = int(input())

    lines = []

    for i in range(num):
        a, b = map(int, input().split())
        lines.append([a, b])
    
    lines.sort()
    # print(lines)
    # A = []
    # B = []
    # for a, b in lines:
    #     A.append(a)
    #     B.append(b)
    # print(A)
    # print(B)

    lis = [1] * num

    for i in range(num):
        for j in range(i):
            if lines[j][1] < lines[i][1]:
                lis[i] = max(lis[j] + 1, lis[i])
    # print(lis)
    print(num - max(lis))

if __name__ == "__main__":
    solution()