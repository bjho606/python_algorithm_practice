# DFS/BFS lv.3

import sys
input = sys.stdin.readline

def find_group_dfs(node, depth):
    global answer, visited, connection
    if not visited[node]:
        visited[node] = 1
        for next_node in connection[node]:
            find_group_dfs(next_node, depth+1)
        if depth == 0:
            answer += 1
    
    return

def solution(n, computers):
    global answer, visited, connection
    answer = 0
    
    connection = [[] * (n+1) for _ in range(n+1)]
    for cur_i, computer in enumerate(computers):
        for connected_i, connected_node in enumerate(computer):
            # print(cur_i, connected_i)
            if cur_i != connected_i and connected_node == 1:
                connection[cur_i+1].append(connected_i+1)
    # print(connection)
    visited = [0] * (n+1)
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        find_group_dfs(i, 0)

    print(answer)
    return answer

if __name__ == "__main__":
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])  # return 2