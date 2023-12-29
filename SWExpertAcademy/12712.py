# 파리퇴치 3 (배열제어)

import sys
input = sys.stdin.readline

directions = {
    '+' : ((0,1), (0,-1), (1,0), (-1,0)),
    'x' : ((1,1), (1,-1), (-1,1), (-1,-1))
}

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    flies = []
    for i in range(N):
        temp = list(map(int, input().split()))
        flies.append(temp)
    # print(flies)

    def spray(flies, i, j):
        catch = 0
        for dirs in directions:
            sums = flies[i][j]

            for dir in directions[dirs]:
                dx, dy = dir
                for t in range(1, M):
                    if 0 <= i + dx*t < N and 0 <= j + dy*t < N:
                        sums += flies[i + dx*t][j + dy*t]

            catch = max(catch, sums)
        return catch

    max_catch = 0
    for i in range(N):
        for j in range(N):
            catch = spray(flies, i, j)
            max_catch = max(max_catch, catch)

    print(f'#{test_case} {max_catch}')