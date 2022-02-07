# 최소공배수 = 두 수 곱 / 최대공약수

def gcd(a, b):
    n1 = max(a, b)
    n2 = min(a, b)
    while(n2 != 0):
        temp = n1 % n2
        n1 = n2
        n2 = temp

    return n1

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    lcm = int(a*b/gcd(a, b))
    print(lcm)