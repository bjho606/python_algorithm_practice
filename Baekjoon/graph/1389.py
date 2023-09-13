# 케빈 베이컨의 6단계 법칙

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    # relations = [[0] * (N+1) for _ in range(N+1)]
    relations = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())

        # relations[a][b] = 1
        # relations[b][a] = 1
        relations[a].append(b)
        relations[b].append(a)
    # print(relations)

    min_boj = 100

    def boj(start_i):
        boj_sum = 0
        boj_counts = [100] * (N+1)
        
        queue = [(start_i, 0)]

        while queue:
            next_i, count = queue.pop(0)

            if boj_counts[next_i] > count:
                boj_counts[next_i] = count
                queue.extend([(i, count+1) for i in relations[next_i]])

        boj_sum = sum(boj_counts[1:])
        # print(boj_sum)

        return boj_sum

    for boj_i in range(1, N+1):
        boj_result = boj(boj_i)
        if boj_result < min_boj:
            answer = boj_i
            min_boj = boj_result
    
    print(answer)
if __name__ == "__main__":
    solution()