# 아이템 제작 (다시)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
item_cost = list(map(int, input().split()))
# print(item_cost)
made_cost = {}

for i in range(m):
    item_index, item1, item2 = map(int, input().split())
    made_cost[item_index -1] = {item1, item2}
# print(made_cost)
    
while len(made_cost) > 0:
    # item1, item2 = made_cost.pop()
    # # print(item1, item2)
    id, (item1, item2) = made_cost.popitem()
    # print(id, item1, item2)
    make_cost = item1 + item2
    if item_cost[id] > make_cost:
        item_cost[id] = make_cost

print(item_cost[0])