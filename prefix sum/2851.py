# 슈퍼 마리오

import sys
input = sys.stdin.readline

scores = []
for i in range(10):
    scores.append(int(input()))
# print(scores)

ans = 0
for score in scores:
    ans += score

    if ans == 100:
        break
    
    if ans > 100:
        if ans - 100 > 100 - (ans - score):
            ans -= score
        break

print(ans)