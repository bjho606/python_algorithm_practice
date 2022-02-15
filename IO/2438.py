# 별 찍기 (2438, 2439, 2440, 2441, 2442, 2445, 2446, 2522, 10991, 10992)

import sys

N = int(sys.stdin.readline())
# for i in range(N):
#     print('*' * (i+1))

# for i in range(N):
#     print(' '*(N-i-1) + '*'*(i+1))

# for i in range(N, 0, -1):
#     print('*' * i)

# for i in range(N):
#     print(' ' * i + '*' * (N - i))

# for i in range(N):
#     print(' ' * (N-i-1) + '*' * (2*i+1))

# for i in range(N):
#     print('*' * (i+1) + ' ' * (2*(N-i-1)) + '*' * (i+1))
# for i in range(N):
#     if i == 0: continue
#     print('*' * (N-i) + ' ' * (2*i) + '*' * (N-i))

# for i in range(N):
#     print(' ' * i + '*' * (2*(N-i)-1))
# for i in range(N):
#     if i == 0: continue
#     print(' ' * (N-i-1) + '*' * (2*(i+1)-1))

# for i in range(N):
#     print(' ' * (N-i-1) + '*' * (i+1))
# for i in range(N):
#     if i == 0: continue
#     print(' ' * i + '*' * (N-i))

# for i in range(N):
#     print(' ' * (N-i-1), end='')
#     for j in range(i+1):
#         print('* ', end='')
#     print()

for i in range(N):
    if i == N-1:
        print('*' * (2*N-1))
        break
    print(' ' * (N-i-1) + '*', end='')
    if i == 0:
        print()
        continue
    print(' ' * (2*i-1), end='')
    print('*')