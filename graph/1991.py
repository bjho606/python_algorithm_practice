# 트리 순회

import sys
input = sys.stdin.readline

# 방법 1 (using class)
# class Node:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right

# def preorder(node):
#     print(node.val, end='')
#     if node.left != '.':
#         preorder(tree[node.left])
#     if node.right != '.':
#         preorder(tree[node.right])

# def inorder(node):
#     if node.left != '.':
#         inorder(tree[node.left])
#     print(node.val, end='')
#     if node.right != '.':
#         inorder(tree[node.right])

# def postorder(node):
#     if node.left != '.':
#         postorder(tree[node.left])
#     if node.right != '.':
#         postorder(tree[node.right])
#     print(node.val, end='')

# 방법 2
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

N = int(input())
tree = {}

for _ in range(N):
    # 방법 1
    # node, left, right = map(str, input().rstrip('\n').split())
    # tree[node] = Node(node, left, right)
    # 방법 2
    root, left, right = map(str, input().rstrip('\n').split())
    tree[root] = [left, right]
# print(tree)

# 방법 1 (using class)
# preorder(tree['A'])
# print()
# inorder(tree['A'])
# print()
# postorder(tree['A'])
# print()

# 방법 2 (using iterative)
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()