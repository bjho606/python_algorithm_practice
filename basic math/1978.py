# 소수 찾기

def check_prime(a):
    count = 0
    temp = a-1

    if a == 1:
        return 0
    elif a == 2:
        return 1

    while temp != 1:
        if a % temp == 0:
            count += 1
            break

        temp -= 1

    if count != 0:
        return 0
    else:
        return 1

N = int(input())
nums = list(map(int, input().split()))
count_prime = 0

for i in range(N):
    count_prime += check_prime(nums[i])

print(count_prime)