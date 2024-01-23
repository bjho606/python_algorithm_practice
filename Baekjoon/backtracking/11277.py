# 2-SAT-1

import sys
from itertools import product
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    # print(True & True)
    # print(True & False)
    # print(False & False)
    # print(True | True)
    # print(True | False)
    # print(False | False)
    # print(1 & 1)
    # print(1 & -1)
    # print(-1 & -1)
    # print(1 | 1)
    # print(1 | -1)
    # print(-1 | -1)

    ans = 0
    
    bool_calc = []
    for i in range(M):
        x, y = map(int, input().split())
        # print( x & y)
        bool_calc.append((x,y))
    # print(bool_calc)
        
    for combi in product([1, -1], repeat=N):
        flag = 1
        # print(combi)

        for bool in bool_calc:
            x, y = bool
            x *= combi[abs(x)-1]
            y *= combi[abs(y)-1]

            flag = flag | (x & y)
        if flag > 0:
            ans = 1
            break

    print(ans)
    # print(1 | (-1&-1 | (1&1)))

if __name__ == "__main__":
    solution()