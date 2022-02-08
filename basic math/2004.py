# 조합 0의 개수

# 시간 초과
# def facto(n):
#     if n == 1 or n == 0:
#         return 1
#     facto = 1
#     for i in range(1, n+1):
#         facto *= i
    
#     return facto

# n, m = map(int, input().split())
# cal = facto(n) // (facto(n-m) * facto(m))
# # print(cal)
# cal = str(cal)
# count = 0
# for i in reversed(cal):
#     if i == '0':
#         count += 1
#     else: break
# print(count)

def two_count(n):
    two = 0

    while n != 0:
        n = n // 2
        two += n

    return two

def five_count(n):
    five = 0

    while n != 0:
        n = n // 5
        five += n

    return five

n, m = map(int, input().split())
result = min(two_count(n) - two_count(m) - two_count(n-m), five_count(n) - five_count(m) - five_count(n-m))
print(result)