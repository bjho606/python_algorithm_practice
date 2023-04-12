# 완전 탐색 (lv.2)

import sys
input = sys.stdin.readline

def n_count_dfs(node, node_arr, visited):
    visited[node] = 1
    
    # 연결이 있으면.. 어디까지 연결되어있는지 확인
    if node_arr[node]:
        for next_node in node_arr[node]:
            if not visited[next_node]:
                # print(node, next_node)
                visited[next_node] = 1
                n_count_dfs(next_node, node_arr, visited)
    
    return visited

def solution(n, wires):
    answer = n-1
    
    node_arr = [[] for _ in range(n+1)]
    for wire in wires:
        node1, node2 = wire
        node_arr[node1].append(node2)
        node_arr[node2].append(node1)
    # print(node_arr)
    
    for wire_to_cut in wires:
        cut_node1, cut_node2 = wire_to_cut
        # print(wire_to_cut)
        # 전선 끊기
        node_arr[cut_node1].remove(cut_node2)
        node_arr[cut_node2].remove(cut_node1)
        # temp_wires = wires.remove(wire_to_cut)
        visited = [0] * (n+1)
        
        after_visited = n_count_dfs(1, node_arr, visited)
        # print(after_visited)
        tree1 = sum(after_visited)
        # print(tree1)
        tree2 = n - tree1
        # print(tree1, tree2)
        
        answer = min(answer, abs(tree1 - tree2))
        
        # 전선 다시 붙이기
        node_arr[cut_node1].append(cut_node2)
        node_arr[cut_node2].append(cut_node1)
    
    return answer

if __name__ == "__main__":
    solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])  # return 3