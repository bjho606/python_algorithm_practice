# 최대공약수, 최소공배수

def gcd(a, b):
    value = min(a, b)
    while value > 1:
        if a % value == 0 and b % value == 0:
            break
        value -= 1

    return value
    
def lcm(a, b):
    value = max(a, b)
    while value <= a * b:
        if value % a == 0 and value % b == 0:
            break
        value += 1

    return value

a, b = map(int, input().split())
print(gcd(a, b), lcm(a, b), sep='\n')
