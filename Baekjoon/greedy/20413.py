# MVP 다이아몬드 (easy)

import sys
input = sys.stdin.readline

rank_seq = {
    'B' : 0,
    'S' : 1,
    'G' : 2,
    'P' : 3,
    'D' : 4
}

N = int(input())
s, g, p, d = map(int, input().split())
# rank_bound = [s, g, p, d]
rank_bound = [s-1, g-1, p-1, d-1, d]
# print(rank_bound)
ranks = list(input().rstrip())
# print(rank)

MAX_MONTHLY_MONEY = d

answer = 0
ago = 0
if ranks[0] == 'D':
    ago = MAX_MONTHLY_MONEY
else:
    ago = rank_bound[rank_seq[ranks[0]]]
answer += ago

for i, cur_rank in enumerate(ranks):
    if i == 0:
        continue

    if cur_rank == 'D':
        cur = MAX_MONTHLY_MONEY
    else:
        cur = rank_bound[rank_seq[cur_rank]] - ago
    answer += cur
    ago = cur

print(answer)