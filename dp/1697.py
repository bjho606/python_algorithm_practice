# 숫자놀이

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
ints = list(map(int, input().split()))
K = int(input())

ans = 1
max_num = ints[-1] * K + 1
able = [0] * max_num

def print_answer():
    winner = ""
    for i in range(1, max_num):
        if able[i] == 0:
            if i % 2 == 0: winner = "holsoon"
            else: winner = "jjaksoon"

            print('{} win at {}'.format(winner, i))
            return

# 시간 초과
def sol_dfs():
    def dfs(num, depth):
        able[num] = 1
        if depth >= K: return

        for next in ints:
            dfs(num + next, depth+1)
        
    dfs(0, 0)

    print_answer()

# 메모리 초과
def sol_bfs():
    q = deque()

    def bfs(num, depth):
        q.append((num, 0))

        while q:
            next, depth = q.popleft()
            able[next] = 1
            
            if depth > K: break

            for i in range(N):
                q.append((next + ints[i], depth+1))

    bfs(0, 0)

    print_answer()

def sol_dp():
    for i in ints:
        able[i] = 1

    dp = [set() for _ in range(K+1)]
    dp[1] = set(ints)

    for i in range(2, K+1):
        before = dp[i-1]
        for before_num in before:
            for num in ints:
                able[before_num + num] = 1
                dp[i].add(before_num + num)

    print_answer()

# sol_dfs()
# sol_bfs()
sol_dp()