# 스도쿠 검증 (완전탐색)

import sys
input = sys.stdin.readline

T = int(input())

def sudoku_result(board):
    def check_3by3(board, start_i, start_j):
        num_set = set()
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if board[i][j] not in num_set:
                    num_set.add(board[i][j])
                else:
                    return False

        return True
    
    def check_width(board, start_i):
        num_set = set()
        for i in range(9):
            if board[start_i][i] not  in num_set:
                num_set.add(board[start_i][i])
            else:
                return False
        
        return True

    def check_height(board, start_i):
        num_set = set()
        for i in range(9):
            if board[i][start_i] not  in num_set:
                num_set.add(board[i][start_i])
            else:
                return False
        
        return True

    # 3X3 체크
    for i in range(3):
        for j in range(3):
            if check_3by3(board, 3*i, 3*j) == False:
                return False
            
    # 전체 가로 세로 체크
    for w in range(9):
        if check_width(board, w) == False:
            return False

    for h in range(9):
        if check_height(board, h) == False:
            return False
        
    return True

for test_case in range(1, T + 1):
    board = []
    for i in range(9):
        t = list(map(int,input().split()))
        board.append(t)
    # print(board)

    if sudoku_result(board) == True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')