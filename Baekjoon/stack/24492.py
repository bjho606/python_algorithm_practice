# Cow Frisbee

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    heights = list(map(int, input().split()))

    ans = 0

    stack = []
    for right_i, height in enumerate(heights):
        while stack and stack[-1][1] < height:
            stack.pop()
        if stack:
            ans += right_i - stack[-1][0] + 1

        stack.append((right_i, height))

    stack = []
    for right_i, height in enumerate(reversed(heights)):
        while stack and stack[-1][1] < height:
            stack.pop()
        if stack:
            ans += right_i - stack[-1][0] + 1

        stack.append((right_i, height))

    print(ans)

if __name__ == "__main__":
    solution()