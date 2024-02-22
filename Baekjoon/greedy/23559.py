# 밥

import sys
input = sys.stdin.readline

"""
N = 10^5
X = 5*10^8
A,B = 10^4
완탐 : 2^N
"""
"""
[의식의 흐름]
1. 일단 가치가 큰 순으로 하나씩 넣었다가 안되서 뺄때, 어떤걸 빼는게 가장 덜 손해일까?
-> 가치가 가장 적게 줄어드는 경우
-> = 두 가치의 차이가 가장 적은 경우
-> 그럼 반대로 하나씩 넣을 때, 가치 차이가 큰 순으로 넣는게??
2. 순서 : 가치 차이가 큰 순으로 5000 vs 1000 중 골라서 넣기
    1) 만약 5000원을 넣어도 될 정도로 돈이 남아 있다면(= 나머지를 모두 1000원 뽑는 경우) 둘 중 더 큰 가치를 넣기
    2) 아니라면 1000원짜리 뽑아
"""

def solution():
    N, X = map(int, input().split())

    menu = []
    for i in range(N):
        menu.append(list(map(int, input().split())))
    # print(menu)
    menu = sorted(menu, key=lambda x: -abs(x[0]-x[1]))
    # print(menu)

    chosen = []
    for i, (a, b) in enumerate(menu):
        # 만약 이번에 5000원짜리르 뽑아도 될 정도로 돈이 남아있다면
        if (5000 + (N-1-i) * 1000 <= X):
            # a 와 b를 비교해서 더 큰 가치를 pick
            if a > b:
                chosen.append(a)
                X -= 5000
            else:
                chosen.append(b)
                X -= 1000
        # 무조건 1000원짜리 뽑아야지
        else:
            chosen.append(b)
            X -= 1000
    # print(chosen)

    print(sum(chosen))

if __name__ == "__main__":
    solution()