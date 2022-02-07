# 최대공약수 - 유클리드 호제법

def gcd(a, b):
    n1 = max(a, b)
    n2 = min(a, b)
    while(n2 != 0):
        temp = n1 % n2
        n1 = n2
        n2 = temp

    return n1

a_count, b_count = map(int, input().split())

one_count = gcd(a_count, b_count)

print('1' * one_count)