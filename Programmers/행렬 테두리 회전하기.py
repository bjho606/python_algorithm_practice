from collections import deque

def rotate(query, board):
    x1, y1, x2, y2 = query
    temp = board[x1][y1]
    temp_arr = [temp]

    for i in range(x1, x2):
        # print(i, board[i][y1], board[i+1][y1])
        board[i][y1] = board[i+1][y1]
        temp_arr.append(board[i][y1])

    for i in range(y1, y2):
        board[x2][i] = board[x2][i+1]
        temp_arr.append(board[x2][i])

    for i in range(x2, x1, -1):
        board[i][y2] = board[i-1][y2]
        temp_arr.append(board[i][y2])
    
    for i in range(y2, y1, -1):
        board[x1][i] = board[x1][i-1]
        temp_arr.append(board[x1][i])

    board[x1][y1+1] = temp

    # 확인
    # for i in board:
    #     print(i)

    return min(temp_arr), board

def solution(rows, columns, queries):
    answer = []
    board = [[0]*(columns+1)]
    for i in range(rows):
        board += [[0] + list(j+i*columns for j in range(1, columns + 1))]
    # for i in board:
    #     print(i)

    for query in queries:
        
        # 회전
        min_ans, board = rotate(query, board)
        
        # 가장 작은 숫자answer에 넣기
        answer.append(min_ans)

    print(answer)
    return answer

solution(6, 7, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100, 97, [[1,1,100,97]])