# N-Queen

import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    row = [0] * N
    count = 0

    def bt(cur_row):
        nonlocal count 

        if cur_row == N:
            count += 1
            return
        
        # 각 줄의 모든 칸에 퀸을 배치해본다.
        for i_queen in range(N):
            row[cur_row] = i_queen

            # 해당 줄 위의 칸들을 확인한다.
            flag = False
            for prev_row in range(cur_row):
                if row[prev_row] == i_queen:        # 세로선 중복
                    flag = True
                    break
                if abs(cur_row - prev_row) == abs(row[cur_row] - row[prev_row]):    # 대각선 중복
                    flag = True
                    break
            if flag: continue

            # 걸리는게 없으면 다음 칸 ㄱ
            bt(cur_row + 1)

    bt(0)

    # print(row)
    print(count)

if __name__ == "__main__":
    solution()