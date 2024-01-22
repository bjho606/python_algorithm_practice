# N과 M (10)

import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    ans_arr = set()

    def bt(i, depth):
        nonlocal arr, n, m

        if depth == m:
            # print(arr)
            ans_arr.add(tuple(arr))
            return
        
        depth += 1

        for t in range(i, n):
            arr.append(a[t])
            bt(t+1, depth)
            arr.pop(-1)

    arr = []
    bt(0, 0)    # index, depth

    # print(sorted(ans_arr))
    for ans in sorted(ans_arr):
        print(*ans)

if __name__ == "__main__":
    solution()