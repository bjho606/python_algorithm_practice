# 프린터 큐

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = 0
    importance = list(map(int, input().split()))
    # print(importance)
    while True:
        if importance[0] == max(importance):
            ans += 1
            importance.pop(0)
            if M == 0:
                print(ans)
                break
            else:
                M -= 1
        else:
            importance.append(importance.pop(0))
            if M == 0:
                M = len(importance) - 1
            else:
                M -= 1