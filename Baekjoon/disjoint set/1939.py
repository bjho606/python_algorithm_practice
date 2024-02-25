# 중량제한

"""
1. union-find 를 써서 연결을 시키는거 같은데,
2. 뭔가 여러개가 연결되었을 때 최소 가중치(=중량)를 초과하는 무게가 단 하나라도 존재해서는 안됨
3. 그럼 중량이 큰 순으로 정렬!
4. 간선을 하나씩 꺼내면서 연결을 시켜보자. 
5. 지금 꺼낸 간선으로 인해 목표 점들이 연결되었다면, 마지막에 꺼낸 무게가 결국 답 (어차피 이 길을 지나야하니까)
"""

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    parent = [i for i in range(N+1)]
    edgeInfos = []

    def find(n):
        if parent[n] == n: return n
        parent[n] = find(parent[n])
        return parent[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)

        parent[max(root1, root2)] = min(root1, root2)

    def isConnected(n1, n2):
        return find(n1) == find(n2)

    for _ in range(M):
        a, b, c = map(int, input().split())
        edgeInfos.append([a, b, c])
    # print(edgeInfos)

    node1, node2 = map(int, input().split())

    edgeInfos.sort(key=lambda x: -x[2])
    # print(edgeInfos)
    
    for info in edgeInfos:
        n1, n2, limit = info
        union(n1, n2)

        if isConnected(node1, node2):
            print(limit)
            break
        # print(parent)

if __name__ == "__main__":
    solution()