# 핸들 뭘로 하지

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def solution():
    N = int(input())

    word = list(input().rstrip('\n'))
    # print(word)

    relations = [[] for _ in range(N)]

    for i in range(N-1):
        u, v = map(int, input().split())

        relations[u-1].append(v-1)
        relations[v-1].append(u-1)
    # print(relations)

    ans = word[0]
    visited = [0 for _ in range(N)]
    visited[0] = 1
    queue = deque()
    queue.append(([0], 1))

    max_length = 1
    cur_word = 'a'

    while queue:
        index_list, length = queue.popleft()

        if max_length != length:
            ans += cur_word
            length += 1
            cur_word = 'a'
        
        next_index_list = []

        for cur_index in index_list:
            for next_index in relations[cur_index]:
                if not visited[next_index]:
                    if cur_word == word[next_index]:
                        next_index_list.append(next_index)
                    elif cur_word < word[next_index]:
                        next_index_list = [next_index]
                        cur_word = word[next_index]
                    
                    visited[next_index] = 1
        
        if next_index_list:
            queue.append((next_index_list, length + 1))

    # [시간초과]
    # def dfs(cur_handle, cur_node, depth, visited):
    #     nonlocal ans
    #     if len(relations[cur_node]) < 0 or depth >= N:
    #         if ans < cur_handle:
    #             ans = cur_handle
    #         return

    #     isEnd = True

    #     next_candidates = []
    #     for next_node in relations[cur_node]:
    #         if not visited[next_node]:
    #             next_candidate = word[next_node]
    #             if next_candidates:
    #                 if next_candidate > next_candidates[0][0]:
    #                     next_candidates = [(next_candidate, next_node)]
    #                 elif next_candidate == next_candidates[0][0]:
    #                     next_candidates.append((next_candidate, next_node))
    #             else:
    #                 next_candidates = [(next_candidate, next_node)]

    #     for next_word, next_node in next_candidates:
    #         if not visited[next_node]:
    #             visited[next_node] = 1
    #             dfs(cur_handle+next_word, next_node, depth + 1, visited)
    #             # visited[next_node] = 0

    #             isEnd = False

    #     if isEnd:
    #         if ans < cur_handle:
    #             ans = cur_handle
    #         return

    # visited[0] = 1
    # dfs(word[0], 0, 0, visited)

    print(ans)

if __name__ == "__main__":
    solution()