# 소수 구하기

M, N = map(int, input().split())

for num in range(M, N+1):
    if(num == 1):
        continue
    prime = 0
    for j in range(2, int(num**0.5)+1):
        if num%j == 0:
            prime += 1
            break
    if prime == 0:
        print(num)