# Two Dots

import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution():
    isCycle = False

    N, M = map(int, input().split())

    board = []
    for i in range(N):
        board.append(list(input().strip()))
    # print(board)
    
    dotType_count = 1
    visited = [[0]*M for _ in range(N)]

    def find_cycle(x, y, dotType_count, dotType, prev_dir):
        nonlocal visited

        result = False

        visited[x][y] = dotType_count

        temp = False
        for d in range(4):
            next_x, next_y = x + dx[d], y + dy[d]

            # 예외
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M: continue
            if board[next_x][next_y] != dotType: continue
            
            # 첫 시작은 제외
            if prev_dir != -1:
                # 사이클 발견 여부
                if visited[next_x][next_y] == dotType_count:
                    # 방향이 반대면 바로 전꺼
                    if abs(prev_dir - d) == 2:
                        continue
                    # 방향이 다르면 성공!
                    else:
                        result = True
                        return result

            # go next
            if not visited[next_x][next_y]:
                temp = find_cycle(next_x, next_y, dotType_count, dotType, d)

        if temp:
            result = True

        return result

    flag = False
    for i in range(N):
        if flag: break
        for j in range(M):
            if flag: break
            if not visited[i][j]:
                isCycle = find_cycle(i, j, dotType_count, board[i][j], -1)
                dotType_count += 1
                if isCycle:
                    flag = True
                    break

    # for i in range(N):
    #     print(visited[i])

    if isCycle:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    solution()