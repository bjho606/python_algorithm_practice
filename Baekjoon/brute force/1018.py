# 체스판 다시 칠하기

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(input().rstrip())

    def repaint(start_i, start_j):
        count = 0
        start_letter = board[start_i][start_j]
        board_temp = []
        if start_letter == 'B':
            for _ in range(4):
                board_temp.append('BWBWBWBW')
                board_temp.append('WBWBWBWB')
        else:
            for _ in range(4):
                board_temp.append('WBWBWBWB')
                board_temp.append('BWBWBWBW')
        
        for i in range(8):
            for j in range(8):
                if board_temp[i][j] != board[start_i+i][start_j+j]:
                    count += 1

        return min(count, 64-count)
    
    count_repaint = 64
    for i in range(N-7):
        for j in range(M-7):
            count_repaint = min(count_repaint, repaint(i, j))
    
    print(count_repaint)

if __name__ == "__main__":
    solution()