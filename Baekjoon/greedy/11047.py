# 동전 0

import sys

N, K = map(int, sys.stdin.readline().split())
A = []
for i in range(N):
    A.insert(0, int(sys.stdin.readline()))

count = 0

for i in range(len(A)):
    if A[i] <= K:
        count += (K//A[i])
        K = K % A[i]

# 시간 초과
# while K > 0:
#     for i in range(len(A)):
#         if A[i] <= K:
#             count += 1
#             K -= A[i]
#             break
        
print(count)