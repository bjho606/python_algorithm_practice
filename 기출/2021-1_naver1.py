# 부족한 금액 계산하기

import sys
input = sys.stdin.readline

def solution(price, money, count):
    answer = 0
    need_total = 0
    for nth in range(1, count + 1):
        need_total += nth * price

    left_money = money - need_total

    if left_money >= 0:
        answer = 0
    else:
        answer = -left_money

    print(answer)
    return answer

if __name__ == "__main__":
    solution(3, 20, 4) # return 10