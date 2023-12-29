# 숫자 배열 회전

import sys
input = sys.stdin.readline
import numpy as np

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        board.append(temp)
    # print(board)

    print(f'#{test_case}')

# [numpy로 푸는 법] - import numpy as np
    # b = np.array(board)
    # r_90 = np.rot90(b, -1)
    # r_180 = np.rot90(b, -2)
    # r_270 = np.rot90(b, -3)

    # b_90 = r_90.tolist()
    # b_180 = r_180.tolist()
    # b_270 = r_270.tolist()
    
# [zip로 푸는 법]
    # def rotate_90(board):
    #     reversed = board[::-1]
    #     rotated = list(zip(*reversed))

    #     return rotated
        
    # b_90 = rotate_90(board)
    # b_180 = rotate_90(b_90)
    # b_270 = rotate_90(b_180)

# [일반적으로 푸는 법]
    def rotate_90(board):
        rotated = [[0]*N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                rotated[col][N-1-row] = board[row][col]
        
        return rotated

    def rotate_180(board):
        rotated = [[0]*N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                rotated[N-1-row][N-1-col] = board[row][col]
        
        return rotated
    
    def rotate_270(board):
        rotated = [[0]*N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                rotated[N-1-col][row] = board[row][col]
        
        return rotated
    
    b_90 = rotate_90(board)
    b_180 = rotate_180(board)
    b_270 = rotate_270(board)


# [출력]
    for i in range(N):
        print(''.join(map(str, b_90[i])), ''.join(map(str, b_180[i])), ''.join(map(str, b_270[i])))
        # for j in range(N):
        #     print(b_90[i][j], end='')
        # print(end=' ')
        # for j in range(N):
        #     print(b_180[i][j], end='')
        # print(end=' ')
        # for j in range(N):
        #     print(b_270[i][j], end='')
        # print()