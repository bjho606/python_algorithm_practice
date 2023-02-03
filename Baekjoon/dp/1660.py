# 캡틴 이다솜

import sys

input = sys.stdin.readline

N = int(input())

# tri = [0, 1]
tetra = [0]
for i in range(1, sys.maxsize):
#     # tri.append(i + tri[i-1])
#     # tetra.append(tri[i] + tetra[i-1])
    tetra.append(tetra[i-1] + (i*(i+1)) // 2)
    if tetra[i] >= N:
        break
# print(tri)
# ball = 0
# i = 1
# while ball < N:
#     ball += (i*(i+1)) // 2
#     tetra.append(ball)
#     i += 1
# print(tetra)

MAX = sys.maxsize
dp = [MAX] * (N+1)
for i in range(1, N+1):
    for tet in tetra:
        if tet >= i:
            if tet == i:
                dp[i] = 1
            break
        dp[i] = min(dp[i - tet] + 1, dp[i])

print(dp[N])