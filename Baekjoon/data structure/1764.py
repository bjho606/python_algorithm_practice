# 듣보잡

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    names = []

    n_set = set()
    m_set = set()

    for _ in range(N):
        n_set.add(input().strip())
    for _ in range(M):
        m_set.add(input().strip())
    
    names = list(n_set & m_set)
    
    names.sort()
    print(len(names))
    for name in names:
        print(name)

if __name__ == "__main__":
    solution()