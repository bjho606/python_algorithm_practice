# 탑

import sys
input = sys.stdin.readline

N = int(input())
heights = [0] + list(map(int, input().split()))

ans = [0]
higher = [(0, 100000001)]
cur_i, cur_h = 1, heights[1]

for i in range(2, N+1):
    # 새로운 애가 더 낮으면
    if heights[i] < cur_h:
        ans.append(cur_i)
        higher.append((cur_i, cur_h))
        cur_i, cur_h = i, heights[i]

    # 새로운 애가 더 높으면
    else:
        while higher:
            cur_i, cur_h = higher[-1]
            if heights[i] < cur_h:
                ans.append(cur_i)
                cur_i, cur_h = i, heights[i]
                break
            else:
                higher.pop()

print(*ans)