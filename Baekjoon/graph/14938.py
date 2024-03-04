# 서강그라운드

"""
[아이디어]
1. 각 노드에서 시작하는 경우로 나누어,
2. 해당 경우에서의 시작점부터 각 노드까지의 거리 갱신 => 다익스트라?
3. 방문 가능한 노드들의 아이템들만 합산
"""
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solution():
    n, search_range, r = map(int, input().split())

    edges = [[] for _ in range(n)]
    items = list(map(int, input().split()))
    for i in range(r):
        a, b, l = map(int, input().split())
        edges[a-1].append((b-1, l))
        edges[b-1].append((a-1, l))
    # print(edges)
        
    max_item = 0
    for start_node in range(n):
        visitable = [0] * n
        visitable[start_node] = 1
        values = [INF] * n          # 시작점으로부터의 거리
        values[start_node] = 0

        pq = []
        heapq.heappush(pq, [start_node, values[start_node]])
        while pq:
            cur_node, cur_val = heapq.heappop(pq)

            for next in edges[cur_node]:
                next_node, next_val = next
                sum_val = cur_val + next_val
                if values[next_node] > sum_val:
                    values[next_node] = sum_val
                    heapq.heappush(pq, [next_node, values[next_node]])
                if sum_val <= search_range:
                    visitable[next_node] = 1
            # print(values)
        # print(visitable)
        sum_item = 0
        for i in range(n):
            if visitable[i]:
                sum_item += items[i]
        max_item = max(max_item, sum_item)
    
    print(max_item)

if __name__ == "__main__":
    solution()