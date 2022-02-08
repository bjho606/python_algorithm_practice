# 골드바흐의 추측

def check_prime(n):
    count = 0
    temp = n-1

    if n == 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

while 1:
    n = int(input())
    if n == 0: break

    for i in range(3, n//2 + 1, 2):
        if check_prime(i) == True:
            if check_prime(n-i) == True:
                print("%d = %d + %d" % (n, i, n-i))
                break

# 다른 풀이
# import sys
# input = sys.stdin.readline

# def pn_s(n):
#     for i in range(2, len(pnl)):
#         if pnl[n-i] and pnl[i]:
#             return (f'{n} = {i} + {n - i}')
    
#     return "Goldbach's conjecture is wrong."


# pnl = [1] * 1000001

# for i in range(2, 1001):
#     if pnl[i] != 0:
#         for j in range(2*i, 1000001, i):
#             pnl[j] = 0


# while 1:
#     n = int(input())
#     if n == 0:
#         break
#     result = pn_s(n)
#     print(result)