# 요세푸스 문제

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = deque([i+1 for i in range(N)])
yose = []
idx = 0
while True:
    nums.rotate(-(K-1))
    yose.append(nums[0])
    del nums[0]
    idx += 1
    if len(nums) <= 0:
        break

print('<' + ', '.join(map(str, yose)) + '>')