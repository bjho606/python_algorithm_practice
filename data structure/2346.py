# 풍선 터뜨리기

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

balloon = list(map(int, input().split()))
q = deque(enumerate(balloon))
# print(q)

ans = []

while q:
    idx, num = q.popleft()
    ans.append(idx + 1)
    if num > 0:
        q.rotate(-num+1)
    else:
        q.rotate(-num)

    # print(q)

print(' '.join(map(str, ans)))