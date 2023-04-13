# DFS/BFS lv.2

import sys
input = sys.stdin.readline
from collections import deque

# dfs
def find_way(x, y, length, maps, visited):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    # 지나왔는지 표시 ----- !!!! 여기다 표시하면 시간 초과가 남!
    # visited[x][y] = 1
    
    # 성공
    if x == m-1 and y == n-1:
        answers.append(length)
        visited[x][y] = 0
        return
    
    for d in range(4):
        next_x = x + dx[d]
        next_y = y + dy[d]
        
        # 범위 초과
        if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n:
            continue
        # 길이 아님
        if not maps[next_x][next_y]:
            continue
        # 이미 지나간 길
        if visited[next_x][next_y]:
            continue
        else:
            visited[next_x][next_y] = 1
            # 한칸 이동
            find_way(next_x, next_y, length+1, maps, visited)
    
    # 다른 경로를 위해 지나온길 표시 제거
    visited[x][y] = 0
    
    return

# bfs
def find_way2(x, y, maps, visited):
    global answer
    answer = -1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque()
    queue.append((x, y, 1))
    
    while queue:
        cur_x, cur_y, length = queue.popleft()
        # print(cur_x, cur_y)

#         # 지나왔는지 표시 ----- !!!! 여기다 표시하면 시간 초과가 남!
#         visited[cur_x][cur_y] = 1

        # 성공
        if cur_x == m-1 and cur_y == n-1:
            answer = length
            break
    
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]

            # 범위 초과
            if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n:
                continue
            # 길이 아님
            if maps[next_x][next_y] == 0:
                continue
            # 이미 지나간 길
            if visited[next_x][next_y]:
                continue
            else:
                visited[next_x][next_y] = 1
                # 한칸 이동
                queue.append((next_x, next_y, length+1))

    return answer

def solution(maps):
    global answers, m, n
    m = len(maps)
    n = len(maps[0])
    
    answers = []
    visited = [[0]*n for _ in range(m)]
    # print(visited)
    
    # [DFS]
    # find_way(0, 0, 1, maps, visited)
    # if not answers:
    #     answer = -1
    # else:
    #     answer = min(answers)

    # [BFS]
    find_way2(0, 0, maps, visited)
    # print(answers)
    
    print(answer)
    return answer

if __name__ == "__main__":
    solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])     # return 11