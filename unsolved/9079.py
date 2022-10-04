# 못품.. 이해 안됨.. 다시.. 전혀 몰랐음..
# 동전 게임
# 완전탐색, 비트마스킹
import sys

input = sys.stdin.readline

def find_arr(board):
    global ans

T = int(input())
# for _ in range(T):

board = []
for i in range(3):
    temp = list(input().split())
    for j in range(3):
        if temp[j] == 'T':
            temp[j] = 1
        else:
            temp[j] = 0
    board.append(temp)
# print(board)
ans = 0

find_arr(board)