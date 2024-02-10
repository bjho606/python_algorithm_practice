# 요세푸스 문제 0

import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    people = [i for i in range(1, N+1)]
    ans = []

    cur_i = 0
    while people:
        cur_i = (cur_i + (K-1))%len(people)
        ans.append(str(people.pop(cur_i)))
    # print(ans)
    print('<' + ', '.join(ans) + '>')

if __name__ == "__main__":
    solution()