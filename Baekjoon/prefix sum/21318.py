# 피아노 체조

import sys
input = sys.stdin.readline

N = int(input())
difficulty = [0] + list(map(int, (input().split())))
# print(difficulty)
Q = int(input())

# prefix_sum
prefix_sum = [0]
temp = 0
for i in range(1, N):
    if difficulty[i] > difficulty[i+1]:
        temp += 1
    prefix_sum.append(temp)
prefix_sum.append(temp)    # 맨 마지막은 실수 X
# print(prefix_sum)

for i in range(Q):
    x, y = map(int, input().split())
    mistake = 0

    # 시간 초과
    # for now in range(x, y):
    #     next = now+1
        
    #     if difficulty[now] > difficulty[next]:
    #         mistake += 1
    mistake = prefix_sum[y-1] - prefix_sum[x-1]

    print(mistake)