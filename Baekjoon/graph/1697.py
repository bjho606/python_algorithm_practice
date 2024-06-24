# 숨바꼭질

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    ans = 0
    N, K = map(int, input().split())

    visited = [0]*100001
    next_pos = deque()

    next_pos.append((0, N))

    while next_pos:
        count, cur = next_pos.popleft()

        if cur == K:
            ans = count
            break

        for next in (cur-1, cur+1, cur*2):
            if next < 0 or next > 100000:
                continue
            if visited[next]:
                continue

            next_pos.append((count+1, next))
            visited[next] = 1

    print(ans)

if __name__ == "__main__":
    solution()