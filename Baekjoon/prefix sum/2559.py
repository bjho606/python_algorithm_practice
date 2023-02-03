# 수열
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ints = list(map(int, input().split()))
temp_sum = 0

for i in range(K):
    temp_sum += ints[i]
left, right = 0, K-1

max_sum = max(temp_sum, -10000001)
# print(max_sum)

while True:
    right += 1

    # 종료조건 (오른쪽이 마지막이면)
    if right >= N:
        break

    temp_sum = temp_sum - ints[left] + ints[right]
    max_sum = max(max_sum, temp_sum)

    left += 1
    
    # print(max_sum)

print(max_sum)