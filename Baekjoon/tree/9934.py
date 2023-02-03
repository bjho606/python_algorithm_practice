# 완전 이진 트리

import sys
input = sys.stdin.readline

K = int(input())
node_count = 2**K - 1
building_arr = list(map(int, input().split()))
node_arr = [i for i in range(node_count)]

# print(building_arr)
# print(node_arr)

tree = [[] for _ in range(K)]

def traverse(left_node, right_node, depth):
    cur_node = (left_node + right_node) // 2

    if depth >= K-1:
        # print(cur_node, end=' ')
        tree[depth].append(building_arr[cur_node])
        return

    # print(cur_node)
    # print(building_arr[cur_node])
    tree[depth].append(building_arr[cur_node])

    traverse(left_node, cur_node-1, depth+1)
    traverse(cur_node+1, right_node, depth+1)

traverse(0, node_count, 0)
# print(tree)
for i in range(K):
    for num in tree[i]:
        print(num, end=' ')
    print()