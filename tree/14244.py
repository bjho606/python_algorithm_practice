# [트리 만들기]

import sys
input = sys.stdin.readline

def solution(nodes, leafs):
    leaf_node = 0

    for cur_node in range(leafs-1):
        print(cur_node, leafs-1)
    for cur_node in range(leafs-1, nodes-1):
        print(cur_node, cur_node+1)

if __name__ == "__main__":
    n, m = map(int, input().split())

    solution(n, m)