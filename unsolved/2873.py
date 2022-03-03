# 롤러코스터 (다시)
# greedy

import sys

R, C = map(int, sys.stdin.readline().split())

roller = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    roller[i] = list(map(int, sys.stdin.readline().split()))
print(roller)
# print(visited)

if R % 2 != 0:
    # 행이 홀수개면 모두 방문 가능 (양 옆으로 꼬불)
    for i in range(R):
        for j in range(C):
            if i == R-1 and j == C-1:
                exit()
            if j == C-1:
                print('D', end='')
                continue
            if i % 2 != 0:
                print('L', end='')
            else:
                print('R', end='')
elif C % 2 != 0:
    # 열이 홀수개면 모두 방문 가능 (위 아래로 꼬불)
    for i in range(C):
        for j in range(R):
            if i == R-1 and j == C-1:
                exit()
            if j == C-1:
                print('R', end='')
                continue
            if i % 2 != 0:
                print('U', end='')
            else:
                print('D', end='')
elif R % 2 == 0 and C % 2 == 0:
    # 행, 열이 모두 짝수개면 하나 빼고 방문 가능
    print(-1)
