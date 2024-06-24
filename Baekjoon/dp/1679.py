# 숫자놀이

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    use = list(map(int, input().split()))
    K = int(input())

    ans = 0
    max_num = use[-1] * K + 1
    able = [0] * max_num
    dp = [i for i in range(max_num)]

    for num in use:
        able[num] = 1
        dp[num] = 1

    for num in range(1, max_num):
        if dp[num] > K:
            ans = num
            break

        for using in use:
            next = num + using
            if next >= max_num: continue

            dp[next] = min(dp[next], dp[num] + 1)
    # print(dp)

    winner = "holsoon" if ans % 2 == 0 else "jjaksoon"

    print(f"{winner} win at {ans}")

if __name__ == "__main__":
    solution()